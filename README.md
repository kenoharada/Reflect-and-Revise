# Reflect-and-Revise
Official implementation of "Automated Refinement of Essay Scoring Rubrics for Language Models via Reflect-and-Revise"

## Prepare dataset
```bash
# download asap https://www.kaggle.com/competitions/asap-aes
./dataset/asap-ets
```
    
```bash
# Refine
python inference.py
```

```bash
# evaluate
python evaluate.py
```