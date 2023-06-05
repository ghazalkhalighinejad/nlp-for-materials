import os
import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def transform_json(file_path_1, file_path_2, output_dir):
    # Read JSONs
    json_1 = read_json(file_path_1)
    json_2 = read_json(file_path_2)

    # Convert keys in json_1 and json_2 to lower case for comparison
    if isinstance(json_1, str):
        json_1 = read_json(json_1)
    json_1_lower = {k.lower().replace(' ', '_'): v for k, v in json_1.items()}
    json_2_lower = {outer_k: {k.lower().replace(' ', '_'): v for k, v in inner_dict.items()} for outer_k, inner_dict in json_2.items()}

    for outer_key in json_2_lower:
        for inner_key in json_2_lower[outer_key]:
            if inner_key in json_1_lower:
                json_2_lower[outer_key][inner_key] = json_1_lower[inner_key]

    # Create output file path
    output_file_name = os.path.splitext(os.path.basename(file_path_1))[0] + "_output.json"
    output_file_path = os.path.join(output_dir, output_file_name)

    # Write updated json_2 to file
    write_json(output_file_path, json_2_lower)

# Replace with your folder path and output directory
json_folder_path = '/Users/defnecirci/Desktop/nlp-for-materials/evaluation/characterization_sample_jsons'
json_2_file_path = '/Users/defnecirci/Desktop/nlp-for-materials/schemas/ver1/characterization_method_simplified.json'
output_dir = '/Users/defnecirci/Desktop/nlp-for-materials/evaluation/expected_output'

# Iterate over the files in the folder
for file_name in os.listdir(json_folder_path):
    if file_name.endswith('.json'):
        json_1_file_path = os.path.join(json_folder_path, file_name)
        transform_json(json_1_file_path, json_2_file_path, output_dir)
