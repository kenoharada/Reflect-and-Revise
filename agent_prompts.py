EVALUATION_PROMPT = '''You are an expert rater for a high-stakes English writing exam for second-language learners.
Evaluate the response strictly using the scoring guideline. Choose exactly one score from the scoring guideline's score points.

# Essay Prompt
"""{essay_prompt}"""
# Response
"""{response}"""
# Scoring Guideline
"""{rubric}"""

# Output format (follow exactly)
Rationale: [<<<Brief evidence-based rationale.>>>]
Rating: [<<<One integer score only.>>>]'''


EVALUATION_PROMPT_ASAP = '''You are an expert rater for student essays.
Evaluate the essay strictly using the scoring guideline. Choose exactly one score from the scoring guideline's score points.

# Student Essay
"""{response}"""
# Scoring Guideline
"""{rubric}"""

# Output format (follow exactly)
Rationale: [<<<Brief evidence-based rationale.>>>]
Rating: [<<<One integer score only.>>>]'''

EXAMPLE_FORMAT_ASAP_WITH_RATIONALE = '''Assistant input:
Essay to be rated:
"""{response}"""
Assistant rationale:
"""{rationale}"""
Assistant score:
"""{rating}"""
Desired score:
"""{desired_rating}"""'''

EXAMPLE_FORMAT_ASAP_WITHOUT_RATIONALE = '''Assistant input:
Essay to be rated:
"""{response}"""
Assistant score:
"""{rating}"""
Desired score:
"""{desired_rating}"""'''

EXAMPLE_FORMAT_WITH_RATIONALE = '''Assistant input:
Essay prompt:
"""{essay_prompt}"""
Essay to be rated:
"""{response}"""
Assistant rationale:
"""{rationale}"""
Assistant score:
"""{rating}"""
Desired score:
"""{desired_rating}"""'''

EXAMPLE_FORMAT_WITHOUT_RATIONALE = '''Assistant input:
Essay prompt:
"""{essay_prompt}"""
Essay to be rated:
"""{response}"""
Assistant score:
"""{rating}"""
Desired score:
"""{desired_rating}"""'''

PROMPT_FOR_EVOLUTION_WITH_RATIONALE = """I asked an assistant to grade essays using the scoring guideline below:
```
{current_rubric}
```

Here are grading examples that include the assistant input, the assistant rationale, the assistant score, and the desired score:
```
{examples}
```

Revise the scoring guideline to improve score agreement so the assistant's future ratings align more closely with the desired scores.

Requirements:
1. Use the rationale patterns to identify why the assistant over-scored or under-scored, and improve the scoring guideline guidance accordingly to reduce score mismatches.

Output rules:
- Return only the revised scoring guideline.
- Use exactly one fenced code block with triple backticks.
- Do not include any text before or after the code block."""


PROMPT_FOR_EVOLUTION_WITHOUT_RATIONALE = """I asked an assistant to grade essays using the scoring guideline below:
```
{current_rubric}
```

Here are grading examples that include the assistant input, the assistant score, and the desired score:
```
{examples}
```

Revise the scoring guideline to improve score agreement so the assistant's future ratings align more closely with the desired scores.

Requirements:
1. Use score mismatch patterns to identify where the scoring guideline guidance is insufficient or ambiguous, and revise it to reduce score mismatches.

Output rules:
- Return only the revised scoring guideline.
- Use exactly one fenced code block with triple backticks.
- Do not include any text before or after the code block."""
