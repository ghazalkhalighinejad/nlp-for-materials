#!/bin/bash
#SBATCH -t 5:00:00
#SBATCH --partition=nlplab --gres=gpu:a6000:1 
#SBATCH --job-name="bash"
#SBATCH --output=output/%j.out

python3 -u main.py --api_key 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 --paper_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/L104_splits/experiments.txt --table_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/nshot/characterization_json/characterization_L104_S1_He_2009.json --prompt_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/prompts/2.txt