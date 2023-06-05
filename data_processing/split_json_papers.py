import json
import os
import argparse


# load arguments

parser = argparse.ArgumentParser()  
parser.add_argument('--input_file', type=str, default='input.json', help='input file')  
parser.add_argument('--output_dir', type=str, default='output', help='output directory')
args = parser.parse_args()

if __name__ == '__main__':

    # Load the data from the JSON file
    with open(args.input_file) as f:
        data = json.load(f)

    title = data.get('title', '')
    abstract = data.get('abstract', '')
    body = data.get('body', [])
    doi = data.get('doi', '')
    figures = data.get('figures', [])
    table_captions = data.get('table_captions', [])

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    with open(f'{args.output_dir}/title_and_abstract.txt', 'w') as f:
        f.write(title + '\n' + abstract)

    if table_captions:
        with open(f'{args.output_dir}/table_captions.txt', 'w') as f:
            for table_caption in table_captions:
                f.write(str(table_caption) + '\n')

    if figures:
        with open(f'{args.output_dir}/figures.txt', 'w') as f:
            for figure in figures:
                f.write(str(figure) + '\n')

    for section in body:
        section_title = section[0]
        section_content = section[1]
        if section_title == 'Main' or section_title == 'main' or section_title == 'MAIN':
            with open(f'{args.output_dir}/main.txt', 'w') as f:
                f.write(str(section_content))
        if section_title == 'Introduction' or section_title == 'introduction' or section_title == 'INTRODUCTION':
            with open(f'{args.output_dir}/introduction.txt', 'w') as f:
                f.write(str(section_content))
        if section_title == 'Experimental' or section_title == 'experimental' or section_title == 'EXPERIMENTAL DETAILS':
            with open(f'{args.output_dir}/experiments.txt', 'w') as f:
                f.write(str(section_content))
<<<<<<< HEAD
=======
        if section_title == 'Results and Discussion' or section_title == 'results and discussion' or section_title == 'RESULTS AND DISCUSSION':
            with open(f'{args.output_dir}/results_and_discussion.txt', 'w') as f:
                f.write(str(section_content))
        if section_title == 'Conclusions':
            with open(f'{args.output_dir}/conclusions.txt', 'w') as f:
                f.write(str(section_content))
        
    
    
    

>>>>>>> ea7bea42202d36eb08d912ea96686d9424d366b6
