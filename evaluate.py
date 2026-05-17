from inference import prepare_dataset, evaluate_on_rubric, ASYNC_BATCH_SIZE, get_llm_responses_batch_async, calculate_accuracy, calculate_qwk_for_batch, quality_to_desired_rating
import shutil
import asyncio
import re
import os

FEW_SHOT_EVALUATION_PROMPT = '''You are a rater for writing responses on a high-stakes English language exam for second language learners. You will be provided with a prompt and the test-taker's response. Your rating should be based on the rubric below, following the specified format.

Rubric:
{rubric}

Examples:
{examples}

Here is a new essay to rate.
# Essay Prompt
"""{essay_prompt}"""
# Response
"""{response}"""
# Output format:
Rating: [<<<Your rating here.>>>]'''

FEW_SHOT_EXAMPLE_FORMAT = '''
Essay Prompt:
"""{essay_prompt}"""

Student's essay:
"""{response}"""

Rating: {rating}'''

def make_examples_for_few_shot_evolution(batch, dataset='ets'):
    examples = []
    for i, data in enumerate(batch):
        examples.append(FEW_SHOT_EXAMPLE_FORMAT.format(
            essay_prompt=data["essay_prompt"],
            response=data["response"],
            rating=quality_to_desired_rating(data["answer"], dataset)
        ))
    return examples

def build_inference_run_name(args, include_sampling=True):
    base_name = f'{args.optimize_method.split("_")[0]}_{args.seed_prompt}_{args.with_rationale}_train{args.train_size}_iteration{args.iteration}_top{args.top_k}'
    if not include_sampling:
        return base_name
    batch_sizes_tag = "-".join(map(str, args.batch_sizes))
    return f'{base_name}_bs{batch_sizes_tag}_mc{args.monte_carlo_runs}'

async def evaluate_on_rubric_few_shot(model_name, params, batch, rubric, evaluation_prompt, examples, dataset):
    for data in batch:
        prompt_for_llm = evaluation_prompt.format(
            essay_prompt=data["essay_prompt"],
            response=data["response"],
            rubric=rubric,
            examples=examples
        )
        data['messages'] = [{"role": "user", "content": prompt_for_llm}]
    batch_responses = []
    for i in range(0, len(batch), ASYNC_BATCH_SIZE):
        sub_batch = batch[i:i + ASYNC_BATCH_SIZE]
        responses = await get_llm_responses_batch_async(
            [data['messages'] for data in sub_batch],
            model_name,
            params,
        )
        batch_responses.extend(responses)
    accuracy = calculate_accuracy(batch_responses, batch, dataset)
    qwk = calculate_qwk_for_batch(batch_responses, batch, dataset)
    return batch_responses, accuracy, qwk


def return_inference_rubric_path(args, model_name):
    if args.trial == '0':
        result_dir = './optimization_results'
    else:
        result_dir = f'./optimization_trials/trial_{args.trial}'
    run_name_candidates = [
        build_inference_run_name(args, include_sampling=True),
        build_inference_run_name(args, include_sampling=False),  # backward compatibility
    ]
    for run_name in run_name_candidates:
        candidate_dir = os.path.join(result_dir, args.dataset, model_name.replace('/', '_'), run_name)
        best_rubric_path = os.path.join(candidate_dir, 'best_rubric.txt')
        if os.path.exists(best_rubric_path):
            return best_rubric_path
    raise FileNotFoundError(f"best_rubric.txt not found under run names: {run_name_candidates}")


async def main(args):
    evaluation_prompt, current_rubric, train_data, val_data, test_data = prepare_dataset(args.dataset, args.seed_prompt)
    if args.optimize_method == 'no_optimize':
        pass  # use the provided rubric as is
    else:
        rubric_path = return_inference_rubric_path(args, args.model_name)
        if rubric_path is not None:
            with open(rubric_path, 'r') as f:
                current_rubric = f.read()
        else:
            raise ValueError(f"No rubric found for dataset={args.dataset}, model_name={args.model_name}, method={args.optimize_method}, seed_prompt={args.seed_prompt}")



    # few-shot examples
    if 'few_shot' in args.method:
        evaluation_prompt = FEW_SHOT_EVALUATION_PROMPT
        train_examples = make_examples_for_few_shot_evolution(train_data[:args.few_shot_num], args.dataset)
        examples = '\n'.join(train_examples)
    else:
        examples = ''
        

    model_name = args.model_name
    params = eval(args.api_params)
    if args.trial == '0':
        result_dir = './evaluation_results'
    else:
        os.makedirs('./evaluation_trials', exist_ok=True)
        result_dir = f'./evaluation_trials/trial_{args.trial}'

    os.makedirs(result_dir, exist_ok=True)
    result_dir = os.path.join(result_dir, args.dataset)
    os.makedirs(result_dir, exist_ok=True)
    result_model_name = model_name.replace('/', '_')
    result_dir = os.path.join(result_dir, result_model_name)
    os.makedirs(result_dir, exist_ok=True)

    if args.optimize_method != 'no_optimize':
        run_name = f'{args.method}_{build_inference_run_name(args, include_sampling=True)}'
    else:
        run_name = f'{args.method}_{args.optimize_method.split("_")[0]}_{args.seed_prompt}'
    result_dir = os.path.join(result_dir, run_name)
    os.makedirs(result_dir, exist_ok=True)
    #remove if exists
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.makedirs(result_dir, exist_ok=True)
    # save rubric
    with open(os.path.join(result_dir, 'rubric.txt'), 'w') as f:
        f.write(current_rubric)
    
    params['user'] = f'eval_{args.dataset}_{args.model_name.replace("/", "_")}_{run_name}'
        
    if 'few_shot' in args.method:
        model_responses, test_accuracy, test_qwk = await evaluate_on_rubric_few_shot(
            model_name, params, test_data, current_rubric,
            evaluation_prompt, examples, args.dataset)
    else:
        model_responses, test_accuracy, test_qwk = await evaluate_on_rubric(
            model_name, params, test_data, current_rubric,
            evaluation_prompt, args.dataset)
    
    results = []
    for model_response, data in zip(model_responses, test_data):
        essay_prompt, essay_response, annotated_score = data['essay_prompt'], data['response'], data['answer']
        save_dict = {
            'essay_prompt': essay_prompt,
            'essay_response': essay_response,
            'annotated_score': annotated_score,
            'model_response': model_response
        }
        results.append(save_dict)
    # save results
    import json
    with open(os.path.join(result_dir, 'results.jsonl'), 'w') as f:
        for r in results:
            f.write(json.dumps(r) + '\n')
    
    with open(os.path.join(result_dir, 'accuracy.txt'), 'w') as f:
        f.write(str(test_accuracy))
    with open(os.path.join(result_dir, 'qwk.txt'), 'w') as f:
        f.write(str(test_qwk))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    def positive_int(value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"Expected a positive integer, got: {value}")
        return ivalue

    parser.add_argument('--method', type=str, default='zero_shot', choices=['zero_shot','few_shot'])
    parser.add_argument('--optimize_method', type=str, default='base', choices=['base', 'optimize_with_few_shot', 'no_optimize'])
    parser.add_argument('--trial', type=str, default='0')

    parser.add_argument('--seed_prompt', type=str, choices=['simplest', 'simple', 'expert', 'self'], default='expert')
    parser.add_argument('--model_name', type=str, default='openai/gpt-4.1')
    parser.add_argument('--dataset', type=str, default='asap_1', choices=['ets', 'ets3', 'asap_1', 'asap_2', 'asap_3', 'asap_4', 'asap_5', 'asap_6', 'asap_7', 'asap_8', 'ASAP2'])
    parser.add_argument('--api_params', type=str, default='{"temperature":0.8,"max_tokens":8192}')
    parser.add_argument('--few_shot_num', type=int, default=4)
    parser.add_argument('--with_rationale', type=str, default='True', choices=['True', 'False'])
    parser.add_argument('--iteration', type=int, default=10)
    parser.add_argument('--top_k', type=int, default=3)
    parser.add_argument('--train_size', type=int, default=20)
    parser.add_argument('--batch_sizes', type=positive_int, nargs='+', default=[4, 8, 12])
    parser.add_argument('--monte_carlo_runs', type=positive_int, default=1)
    args = parser.parse_args()
    asyncio.run(main(args))
