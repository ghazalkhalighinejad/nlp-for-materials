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

    for key in data:
        print(key)

    title = data['title']
    abstract = data['abstract']
    body = data['body']
    doi = data['doi']
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
        print(section_title)
        section_content = section[1]
        if section_title.lower() == 'main':
            with open(f'{args.output_dir}/main.txt', 'w') as f:
                f.write(str(section_content))
        elif section_title.lower() == 'introduction':
            with open(f'{args.output_dir}/introduction.txt', 'w') as f:
                f.write(str(section_content))
        elif section_title.lower() in ['experimental', 'experimental details','experimental procedures','experimental procedure','materials and methods','experimental section','materials and experimental procedures','experimental work']:
            with open(f'{args.output_dir}/experiments.txt', 'w') as f:
                f.write(str(section_content))
        elif section_title.lower() == 'results and discussion':
            with open(f'{args.output_dir}/results_and_discussion.txt', 'w') as f:
                f.write(str(section_content))
        elif section_title.lower() == 'conclusions':
            with open(f'{args.output_dir}/conclusions.txt', 'w') as f:
                f.write(str(section_content))
