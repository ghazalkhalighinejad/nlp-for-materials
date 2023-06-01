import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def transform_json(file_path_1, file_path_2, output_file_path):
    # Read JSONs
    json_1 = read_json(file_path_1)
    json_2 = read_json(file_path_2)

    # Convert keys in json_1 and json_2 to lower case for comparison
    json_1_lower = {k.lower().replace(' ', '_'): v for k, v in json_1.items()}
    json_2_lower = {outer_k: {k.lower().replace(' ', '_'): v for k, v in inner_dict.items()} for outer_k, inner_dict in json_2.items()}

    for outer_key in json_2_lower:
        for inner_key in json_2_lower[outer_key]:
            if inner_key in json_1_lower:
                json_2_lower[outer_key][inner_key] = json_1_lower[inner_key]

    # Write updated json_2 to file
    write_json(output_file_path, json_2_lower)

# Replace with your file paths
json_1_file_path = '/Users/defnecirci/Desktop/nlp-for-materials/nshot/characterization_json/characterization_L107_S1_Shen_2007.json'
json_2_file_path = '/Users/defnecirci/Desktop/nlp-for-materials/schemas/ver1/characterization_method_simplified.json'
output_file_path = '/Users/defnecirci/Desktop/nlp-for-materials/nshot/expectedoutputs'

transform_json(json_1_file_path, json_2_file_path, output_file_path)
