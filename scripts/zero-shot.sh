#!/bin/bash
#SBATCH -t 5:00:00
#SBATCH --partition=nlplab --gres=gpu:a6000:1 
#SBATCH --job-name="bash"
#SBATCH --output=output/L107%j.out

python3 -u main.py --api_key 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 --paper_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/splitted_papers/L110/experiments.txt --table_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/schemas/ver1/characterization_method_simplified.json --prompt_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/prompts/2.txt