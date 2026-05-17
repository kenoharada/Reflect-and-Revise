from llm_router import get_llm_response_async, get_llm_responses_batch_async
import asyncio
import re
import os
from rubric_prompts import prepare_asap_rubric, prepare_ets_rubric, prepare_asap2_rubric, ASAP2_PROMPT

from agent_prompts import EVALUATION_PROMPT, PROMPT_FOR_EVOLUTION_WITH_RATIONALE, PROMPT_FOR_EVOLUTION_WITHOUT_RATIONALE, EXAMPLE_FORMAT_WITH_RATIONALE, EXAMPLE_FORMAT_WITHOUT_RATIONALE, EVALUATION_PROMPT_ASAP, EXAMPLE_FORMAT_ASAP_WITH_RATIONALE, EXAMPLE_FORMAT_ASAP_WITHOUT_RATIONALE

from utils import prepare_ets_dataset, prepare_asap_dataset, prepare_asap2_dataset
from sklearn.metrics import cohen_kappa_score
import shutil
ASYNC_BATCH_SIZE = int(os.getenv("ASYNC_BATCH_SIZE", "100"))
ASYNC_CONCURRENCY = int(os.getenv("ASYNC_CONCURRENCY", "40"))

def parse_rating(response):
    # Find the substring after 'Rating:' and then extract all numbers from it
    after = re.search(r'Rating:\s*(.*)', response)
    if not after:
        return None
    nums = re.findall(r'\d+', after.group(1))
    if nums:
        return int(nums[-1])  # Return the last matched number after 'Rating:'
    else:
        return None


def parse_rationale(response):
    match = re.search(r'Rationale:\s*\[?<*(.*?)>*\]?\s*Rating:', response, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return None


def quality_to_rating(quality, dataset='ets'):
    if dataset == 'ets':
        mapping = {
            "high": [5, 4],
            "medium": [3],
            "low": [2, 1]
        }
        return mapping.get(quality, None)
    elif dataset == 'ets3':
        mapping = {
            "high": [3],
            "medium": [2],
            "low": [1]
        }
        return mapping.get(quality, None)
    elif dataset.startswith('asap_'):
        return quality  # direct mapping
    elif dataset == 'ASAP2':
        return quality  # direct mapping
    else:
        return None


def rating_to_quality(rating, dataset='ets'):
    if dataset == 'ets':
        if rating in [5, 4]:
            return "high"
        elif rating == 3:
            return "medium"
        elif rating in [2, 1]:
            return "low"
        else: 
            return None
    elif dataset == 'ets3':
        if rating == 3:
            return "high"
        elif rating == 2:
            return "medium"
        elif rating == 1:
            return "low"
        else:
            return None
    elif dataset.startswith('asap_'):
        return rating  # direct mapping
    elif dataset == 'ASAP2':
        return rating  # direct mapping 
    else:
        return None


def quality_to_desired_rating(quality, dataset='ets'):
    if dataset == 'ets':
        mapping = {
            "high": '4 or 5',
            "medium": '3',
            "low": '1 or 2'
        }
        return mapping.get(quality, None)
    elif dataset == 'ets3':
        mapping = {
            "high": '3',
            "medium": '2',
            "low": '1'
        }
        return mapping.get(quality, None)
    elif dataset.startswith('asap_'):
        return quality  # direct mapping
    elif dataset == 'ASAP2':
        return quality  # direct mapping
    else:
        return None


def scoring(llm_judged_response, quality, dataset='ets'):
    rating = quality_to_rating(quality, dataset)
    parsed_rating = parse_rating(llm_judged_response)
    parsed_rationale = parse_rationale(llm_judged_response)
    if parsed_rating is None:
        print(f"Could not parse rating from response: {llm_judged_response}")
        return None

    if rating is None:
        return None
    
    if dataset == 'ets':
        if parsed_rating in rating:
            return 1
        else:
            return 0
    elif dataset == 'ets3':
        if parsed_rating in rating:
            return 1
        else:
            return 0
    elif dataset.startswith('asap_'):
        if parsed_rating == rating:
            return 1
        else:
            return 0
    elif dataset == 'ASAP2':
        if parsed_rating == rating:
            return 1
        else:
            return 0
    else:
        raise ValueError(f"Unknown dataset: {dataset}")


def quality_to_score_for_qwk(quality, dataset='ets'):
    if dataset == 'ets':
        mapping = {
            "high": 3,
            "medium": 2,
            "low": 1
        }
        return mapping.get(quality, None)
    elif dataset == 'ets3':
        mapping = {
            "high": 3,
            "medium": 2,
            "low": 1
        }
        return mapping.get(quality, None)
    elif dataset.startswith('asap_'):
        return quality  # direct mapping
    elif dataset == 'ASAP2':
        return quality  # direct mapping
    else:
        return None

def parse_new_rubric(response):
    response = response.replace('```markdown\n', '```\n')
    pattern = r'```(.*?)```'
    match = re.search(pattern, response, re.DOTALL)
    if match:
        # Return the last fenced block match instead of the first
        all_matches = re.findall(pattern, response, re.DOTALL)
        if all_matches:
            return all_matches[-1].strip()
    else:
        # If no fenced block is found, return the last part starts with ```
        pattern = r'```(.*?)$' # *? means non-greedy matching
        match = re.search(pattern, response, re.DOTALL)
        if match:
            all_matches = re.findall(pattern, response, re.DOTALL)
            if all_matches:
                last_match = all_matches[-1]
                if len(last_match.strip()) < 100:  # if too short, ignore
                    return None
                return all_matches[-1].strip()
        else:
            return None


def calculate_accuracy(model_responses, batch, dataset='ets'):
    correct = 0
    total = 0
    for i, model_response in enumerate(model_responses):
        if not isinstance(model_response, str):
            print(f"Skipping invalid response at index {i}: {model_response}")
            continue
        data = batch[i]
        score = scoring(model_response, data["answer"], dataset)
        if score is not None:
            correct += score
            total += 1
    if total == 0:
        return 0.0
    return correct / total


def calculate_qwk_for_batch(model_responses, batch, dataset='ets'):
    y_true, y_pred = [], []
    valid_count = 0
    for i, model_response in enumerate(model_responses):
        if not isinstance(model_response, str):
            print(f"Skipping invalid response at index {i}: {model_response}")
            continue
        data = batch[i]
        true_score = quality_to_score_for_qwk(data["answer"], dataset)
        pred_quality = rating_to_quality(parse_rating(model_response), dataset)
        pred_score = quality_to_score_for_qwk(pred_quality, dataset)
        if true_score is not None and pred_score is not None:
            y_true.append(true_score)
            y_pred.append(pred_score)
            valid_count += 1
    if len(y_true) == 0:
        return -1.0
    print(f"Valid pairs for QWK calculation: {valid_count}/{len(batch)}")
    valid_portion = valid_count / len(batch)
    if valid_portion < 0.90:
        print("Warning: Less than 90% valid pairs for QWK calculation.")
        return -1.0
    return cohen_kappa_score(y_true, y_pred, weights='quadratic')


async def evaluate_on_rubric(model_name, params, batch, rubric, evaluation_prompt, dataset):
    for data in batch:
        if dataset == 'ASAP2':
            # essay_prompt = ASAP2_PROMPT.format(
            #     source_text=data["source_text"],
            #     essay_prompt=data["essay_prompt"]
            # )
            # prompt_for_llm = evaluation_prompt.format(
            #     essay_prompt=essay_prompt,
            #     response=data["response"],
            #     rubric=rubric
            # )
            # data['messages'] = [{"role": "user", "content": prompt_for_llm}]
            
            prompt_for_llm = EVALUATION_PROMPT_ASAP.format(
                response=data["response"],
                rubric=rubric,
            )
            data['messages'] = [{"role": "user", "content": prompt_for_llm}]

        else:
            prompt_for_llm = evaluation_prompt.format(
                essay_prompt=data["essay_prompt"],
                response=data["response"],
                rubric=rubric
            )
            data['messages'] = [{"role": "user", "content": prompt_for_llm}]
        # print(prompt_for_llm)
    batch_responses = []
    for i in range(0, len(batch), ASYNC_BATCH_SIZE):
        sub_batch = batch[i:i + ASYNC_BATCH_SIZE]
        responses = await get_llm_responses_batch_async(
            [data['messages'] for data in sub_batch],
            model_name,
            params,
            concurrency=ASYNC_CONCURRENCY,
        )
        batch_responses.extend(responses)
    accuracy = calculate_accuracy(batch_responses, batch, dataset)
    qwk = calculate_qwk_for_batch(batch_responses, batch, dataset)
    return batch_responses, accuracy, qwk


def make_examples_for_rubric_evolution(model_responses, batch, dataset='ets', with_rationale=True):
    examples = []
    for i, model_response in enumerate(model_responses):
        data = batch[i]
        if not isinstance(model_response, str):
            print(f"Skipping invalid response at index {i}: {model_response}")
            continue
        # if dataset == 'ASAP2':
        #     essay_prompt = ASAP2_PROMPT.format(
        #         source_text=data["source_text"],
        #         essay_prompt=data["essay_prompt"]
        #     )
        # else:
        #     essay_prompt = data["essay_prompt"]
        
        # if with_rationale:
        #     examples.append(EXAMPLE_FORMAT_WITH_RATIONALE.format(
        #         essay_prompt=essay_prompt,
        #         response=data["response"],
        #         rationale=parse_rationale(model_response),
        #         rating=parse_rating(model_response),
        #         desired_rating=quality_to_desired_rating(data["answer"], dataset)
        #     ))
        # else:
        #     examples.append(EXAMPLE_FORMAT_WITHOUT_RATIONALE.format(
        #         essay_prompt=essay_prompt,
        #         response=data["response"],
        #         rating=parse_rating(model_response),
        #         desired_rating=quality_to_desired_rating(data["answer"], dataset)
        #     ))
        if dataset == 'ASAP2':
            if with_rationale:
                examples.append(EXAMPLE_FORMAT_ASAP_WITH_RATIONALE.format(
                    response=data["response"],
                    rationale=parse_rationale(model_response),
                    rating=parse_rating(model_response),
                    desired_rating=quality_to_desired_rating(data["answer"], dataset)
                ))
            else:
                examples.append(EXAMPLE_FORMAT_ASAP_WITHOUT_RATIONALE.format(
                    response=data["response"],
                    rating=parse_rating(model_response),
                    desired_rating=quality_to_desired_rating(data["answer"], dataset)
                ))
        else:
            if with_rationale:
                examples.append(EXAMPLE_FORMAT_WITH_RATIONALE.format(
                    essay_prompt=data["essay_prompt"],
                    response=data["response"],
                    rationale=parse_rationale(model_response),
                    rating=parse_rating(model_response),
                    desired_rating=quality_to_desired_rating(data["answer"], dataset)
                ))
            else:
                examples.append(EXAMPLE_FORMAT_WITHOUT_RATIONALE.format(
                    essay_prompt=data["essay_prompt"],
                    response=data["response"],
                    rating=parse_rating(model_response),
                    desired_rating=quality_to_desired_rating(data["answer"], dataset)
                ))
    return examples

def prepare_dataset(dataset_name, seed_prompt='expert'):
    evaluation_prompt = EVALUATION_PROMPT
    if dataset_name == 'ets':
        current_rubric = prepare_ets_rubric(dataset_name, seed_prompt)
        train_data, val_data, test_data = prepare_ets_dataset()
        return evaluation_prompt, current_rubric, train_data, val_data, test_data
    elif dataset_name == 'ets3':
        current_rubric = prepare_ets_rubric(dataset_name, seed_prompt)
        train_data, val_data, test_data = prepare_ets_dataset()
        return evaluation_prompt, current_rubric, train_data, val_data, test_data
    elif dataset_name.startswith('asap_'):
        essay_set = int(dataset_name.split('_')[1])
        train_data, val_data, test_data = prepare_asap_dataset(essay_set)
        current_rubric = prepare_asap_rubric(essay_set, seed_prompt)
        return evaluation_prompt, current_rubric, train_data, val_data, test_data
    elif dataset_name == 'ASAP2':
        current_rubric = prepare_asap2_rubric(seed_prompt)
        train_data, val_data, test_data = prepare_asap2_dataset()
        return evaluation_prompt, current_rubric, train_data, val_data, test_data
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")


import random
import copy
async def main(args):
    args.with_rationale = args.with_rationale == 'True'
    evaluation_prompt, current_rubric, train_data, _, _ = prepare_dataset(args.dataset, args.seed_prompt)
    if args.seed_prompt == 'self':
        # TODO: implement self-generated rubric initialization
        pass

    seed = 1
    random.seed(seed)
    random.shuffle(train_data)
    train_data = copy.deepcopy(train_data[:args.train_size])
    if len(train_data) < 100:
        # upsample to 3x at maximum or until exceeding 100 samples
        train_original_data = copy.deepcopy(train_data)
        upsample_times = 0
        while len(train_data) < 100 and upsample_times < 2:
            train_data.extend(copy.deepcopy(train_original_data))
            upsample_times += 1


    model_name = args.model_name
    params = eval(args.api_params)
    trial = args.trial
    if trial == '0':
        result_dir = './optimization_results'
    else:
        os.makedirs('./optimization_trials', exist_ok=True)
        result_dir = f'./optimization_trials/trial_{trial}'
    batch_sizes_tag = "-".join(map(str, args.batch_sizes))
    run_name = f'{args.optimize_method.split("_")[0]}_{args.seed_prompt}_{args.with_rationale}_train{args.train_size}_iteration{args.iteration}_top{args.top_k}_bs{batch_sizes_tag}_mc{args.monte_carlo_runs}'
    params["user"] = f"{args.dataset}_{model_name.replace('/', '_')}_{run_name}"

    os.makedirs(result_dir, exist_ok=True)
    result_dir = os.path.join(result_dir, args.dataset)
    os.makedirs(result_dir, exist_ok=True)
    result_model_name = model_name.replace('/', '_')
    result_dir = os.path.join(result_dir, result_model_name)
    os.makedirs(result_dir, exist_ok=True)

    result_dir = os.path.join(result_dir, run_name)
    os.makedirs(result_dir, exist_ok=True)
    #remove if exists
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.makedirs(result_dir, exist_ok=True)

    os.makedirs(os.path.join(result_dir, 'rubric_evolutions'), exist_ok=True)
    os.makedirs(os.path.join(result_dir, 'best_rubric'), exist_ok=True)

    max_evolution_steps = args.iteration
    batch_sizes = args.batch_sizes
    monte_carlo_runs = args.monte_carlo_runs
    best_train_accuracy = 0.0
    best_train_qwk = -1.0
    best_rubric = current_rubric
    _, train_accuracy, train_qwk = await evaluate_on_rubric(model_name, params, train_data, current_rubric, evaluation_prompt, args.dataset)

    # save the current rubric
    with open(os.path.join(result_dir, 'initial_rubric.txt'), 'w') as f:
        f.write(current_rubric)
    with open(os.path.join(result_dir, 'best_rubric.txt'), 'w') as f:
        f.write(current_rubric) # initially the best rubric is the current rubric
    # save the train score
    with open(os.path.join(result_dir, 'train_score.txt'), 'w') as f:
        f.write(f"Step 0, Training Accuracy: {train_accuracy}\n")
        f.write(f"Step 0, Training QWK: {train_qwk}\n")
    with open(os.path.join(result_dir, 'train_accuracy.txt'), 'w') as f:
        f.write(f"{train_accuracy}\n")
    with open(os.path.join(result_dir, 'train_qwk.txt'), 'w') as f:
        f.write(f"{train_qwk}\n")

    best_train_accuracy = train_accuracy
    best_train_qwk = train_qwk
    rubric_candidates = []
    top_k_candidates = []
    top_k_candidates.append((current_rubric, train_qwk, train_accuracy))  # (rubric, qwk, accuracy)
    for step in range(max_evolution_steps):
        async def evolve_rubrics_for_candidate(step_idx, mc_idx, k_idx, candidate_rubric):
            train_responses, _, _ = await evaluate_on_rubric(
                model_name, params, train_data, candidate_rubric, evaluation_prompt, args.dataset
            )
            failed_examples = []
            failed_responses = []
            for i, model_response in enumerate(train_responses):
                if not isinstance(model_response, str):
                    print(f"Skipping invalid response at index {i}: {model_response}")
                    continue
                data = train_data[i]
                score = scoring(model_response, data["answer"], args.dataset)
                if score == 0:
                    failed_examples.append(data)
                    failed_responses.append(model_response)
            if len(failed_examples) == 0:
                print("No failed examples, skipping evolution.")
                return []

            async def evolve_for_batch(batch_size):
                derived_seed = seed * 1000000 + step_idx * 10000 + mc_idx * 1000 + k_idx * 100 + batch_size
                rng = random.Random(derived_seed)
                batch_idx = rng.sample(range(len(failed_examples)), min(batch_size, len(failed_examples)))
                # 各スコアで失敗した例をランダムにbatch_size個選ぶ
                quality_buckets = {}
                for i in batch_idx:
                    data = failed_examples[i]
                    quality = data["answer"]
                    if quality not in quality_buckets:
                        quality_buckets[quality] = []
                    quality_buckets[quality].append(i)
                # print("Quality buckets:", quality_buckets)
                # now sample equally from each bucket
                num_qualities = len(quality_buckets)
                per_bucket = max(1, batch_size // num_qualities)
                balanced_batch_idx = []
                for quality, indices in quality_buckets.items():
                    sampled_indices = rng.sample(indices, min(per_bucket, len(indices)))
                    balanced_batch_idx.extend(sampled_indices)
                batch_idx = balanced_batch_idx
                if len(batch_idx) == 0:
                    print("No failed examples in batch, skipping evolution.")
                    return None
                failed_examples_batch = [failed_examples[i] for i in batch_idx]
                failed_responses_batch = [failed_responses[i] for i in batch_idx]
                examples = make_examples_for_rubric_evolution(
                    failed_responses_batch, failed_examples_batch, args.dataset, args.with_rationale
                )
                examples_str = '\n\n'.join(examples)
                if args.with_rationale:
                    prompt_for_evolution = PROMPT_FOR_EVOLUTION_WITH_RATIONALE.format(
                        current_rubric=candidate_rubric,
                        examples=examples_str
                    )
                else:
                    prompt_for_evolution = PROMPT_FOR_EVOLUTION_WITHOUT_RATIONALE.format(
                        current_rubric=candidate_rubric,
                        examples=examples_str
                    )
                # print(prompt_for_evolution)
                evolution_response = await get_llm_response_async(
                    [{"role": "user", "content": prompt_for_evolution}],
                    model_name,
                    params
                )
                new_rubric = parse_new_rubric(evolution_response)
                if new_rubric is None:
                    print("No new rubric proposed")
                    return None
                print("New Rubric proposed:")
                output_path = os.path.join(
                    result_dir,
                    'rubric_evolutions',
                    f'step_{step_idx+1}_mc_{mc_idx}_bs_{batch_size}_top{k_idx+1}.txt'
                )
                with open(output_path, 'w') as f:
                    f.write(new_rubric)
                return new_rubric

            batch_tasks = [evolve_for_batch(batch_size) for batch_size in batch_sizes]
            batch_results = await asyncio.gather(*batch_tasks)
            return [result for result in batch_results if result is not None]

        evolved_count = 0
        if args.model_name.startswith('openai/') or args.model_name.startswith('google/'):
            evolve_tasks = [
                evolve_rubrics_for_candidate(step, mc_idx, k_idx, candidate_rubric)
                for mc_idx in range(monte_carlo_runs)
                for k_idx, (candidate_rubric, _, _) in enumerate(top_k_candidates)
            ]
            # evolve_results = await asyncio.gather(*evolve_tasks) # it easily exceeds rate limits
            evolve_results = []
            print(len(evolve_tasks), "evolution tasks to execute.")
            for i in range(0, len(evolve_tasks), 4):
                batch_tasks = evolve_tasks[i:i+4]
                batch_results = await asyncio.gather(*batch_tasks)
                evolve_results.extend(batch_results)
            print(len(evolve_results), "evolution results obtained.")
            for result_list in evolve_results:
                if len(result_list) > 0:
                    rubric_candidates.extend(result_list)
                    evolved_count += len(result_list)
        else:
            for mc_idx in range(monte_carlo_runs):
                for k_idx, (candidate_rubric, _, _) in enumerate(top_k_candidates):
                    # execute in sequence to avoid rate limits
                    evolve_result = await evolve_rubrics_for_candidate(step, mc_idx, k_idx, candidate_rubric)
                    if len(evolve_result) > 0:
                        rubric_candidates.extend(evolve_result)
                        evolved_count += len(evolve_result)
                
        # evolve_results = await asyncio.gather(*evolve_tasks) # it easily exceeds rate limits
        if evolved_count == 0:
            print("No new rubrics evolved in this step.")
            continue
        for (candidate, _, _) in top_k_candidates:
            rubric_candidates.append(candidate)  # keep previous top candidates
        # Evaluate all rubric candidates on train data
        new_top_k_candidates = []
        if args.model_name.startswith('openai/') or args.model_name.startswith('google/'):
            # deal with every 5 candidates in parallel to avoid rate limits
            eval_tasks = [
                evaluate_on_rubric(model_name, params, train_data, candidate, evaluation_prompt, args.dataset)
                for candidate in rubric_candidates
            ]
            print(len(eval_tasks), "candidates to evaluate.")
            eval_results = []
            for i in range(0, len(eval_tasks), 4):
                batch_tasks = eval_tasks[i:i+4]
                batch_results = await asyncio.gather(*batch_tasks)
                eval_results.extend(batch_results)
            print(len(eval_results), "evaluation results obtained.")
            for idx, candidate in enumerate(rubric_candidates):
                _, candidate_train_accuracy, candidate_train_qwk = eval_results[idx]
                new_top_k_candidates.append((candidate, candidate_train_qwk, candidate_train_accuracy))
        else:
            # execute in sequence to avoid rate limits
            for candidate in rubric_candidates:
                _, candidate_train_accuracy, candidate_train_qwk = await evaluate_on_rubric(
                    model_name,
                    params,
                    train_data,
                    candidate,
                    evaluation_prompt,
                    args.dataset,
                )
                new_top_k_candidates.append((candidate, candidate_train_qwk, candidate_train_accuracy))
        # select top k candidates for next iteration, descending by QWK
        top_k_candidates = []
        top_k_candidates.extend(new_top_k_candidates)
        # print('before sorting candidates:', len(top_k_candidates))
        # print(top_k_candidates)
        top_k_candidates = sorted(top_k_candidates, key=lambda x: x[1], reverse=True)[:args.top_k]
        # print('after sorting candidates:', len(top_k_candidates))
        # print(top_k_candidates)
        rubric_candidates = []  # reset for next iteration

        for k in range(len(top_k_candidates)):
            new_rubric, best_candidate_qwk, accuracy_of_best_candidate = top_k_candidates[k]
            with open(os.path.join(result_dir, 'best_rubric', f'step_{step+1}_top{k+1}.txt'), 'w') as f:
                f.write(new_rubric)
        
        with open(os.path.join(result_dir, 'train_score_top_candidates.txt'), 'a') as f:
            for k in range(len(top_k_candidates)):
                new_rubric, best_candidate_qwk, accuracy_of_best_candidate = top_k_candidates[k]
                f.write(f"Step {step+1}, Top {k+1} Candidate, Training Accuracy: {accuracy_of_best_candidate}\n")
                f.write(f"Step {step+1}, Top {k+1} Candidate, Training QWK: {best_candidate_qwk}\n")
        best_candidate_qwk, accuracy_of_best_candidate = top_k_candidates[0][1], top_k_candidates[0][2]
        with open(os.path.join(result_dir, 'train_accuracy.txt'), 'a') as f:
            f.write(f"{accuracy_of_best_candidate}\n")
        with open(os.path.join(result_dir, 'train_qwk.txt'), 'a') as f:
            f.write(f"{best_candidate_qwk}\n")
        with open(os.path.join(result_dir, 'train_score.txt'), 'a') as f:
            f.write(f"Step {step+1}, Training Accuracy (best candidate): {accuracy_of_best_candidate}\n")
            f.write(f"Step {step+1}, Training QWK (best candidate): {best_candidate_qwk}\n")

        if best_candidate_qwk > best_train_qwk:
            best_train_qwk = best_candidate_qwk
            best_rubric = top_k_candidates[0][0]
            with open(os.path.join(result_dir, 'best_rubric.txt'), 'w') as f:
                f.write(best_rubric)
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    def positive_int(value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"Expected a positive integer, got: {value}")
        return ivalue

    parser.add_argument('--optimize_method', type=str, default='base', choices=['base', 'optimize_with_few_shot'])
    parser.add_argument('--with_rationale', type=str, default='True', choices=['True', 'False'])
    parser.add_argument('--iteration', type=int, default=3)
    parser.add_argument('--trial', type=str, default='0')
    parser.add_argument('--top_k', type=int, default=3)

    parser.add_argument('--seed_prompt', type=str, choices=['simplest', 'simple', 'expert', 'self'], default='expert')
    parser.add_argument('--model_name', type=str, default='openai/gpt-5-mini')
    parser.add_argument('--dataset', type=str, default='asap_1', choices=['ets', 'ets3', 'asap_1','ASAP2'])
    parser.add_argument('--api_params', type=str, default='{"temperature":1.0,"max_tokens":8192}')
    parser.add_argument('--train_size', type=int, default=100)
    parser.add_argument('--batch_sizes', type=positive_int, nargs='+', default=[4, 8, 12])
    parser.add_argument('--monte_carlo_runs', type=positive_int, default=1)
    args = parser.parse_args()
    asyncio.run(main(args))
