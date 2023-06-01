#!/bin/bash
#SBATCH -t 5:00:00
#SBATCH --partition=nlplab --gres=gpu:a6000:1 
#SBATCH --job-name="bash"
#SBATCH --output=output/one-shot-L107%j.out

python3 -u main.py \
--api_key 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 \
--paper_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/splitted_papers/L110/experiments.txt \
--table_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/schemas/ver1/characterization_method_simplified.json \
--prompt_path /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/prompts/one-shot.txt \
--paper_path1 /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/splitted_papers/L104/experiments.txt \
--table_path1 /usr/xtmp/gk126/nlp-for-materials/nlp-for-materials/nshot/characterization_json/characterization_L104_S1_He_2009.json