import json
import os

def get_characterization(json_file):
    with open(json_file) as f:
        data = json.load(f)
        
        if "PolymerNanocomposite" in data and "CHARACTERIZATION" in data["PolymerNanocomposite"]:
            return data["PolymerNanocomposite"]["CHARACTERIZATION"]
        
        else:
            print(f"CHARACTERIZATION not found in the JSON data for file: {json_file}")
            return None


def process_all_json_in_folder(input_folder_path, output_folder_path):
    # Get all files in the directory
    files = os.listdir(input_folder_path)

    # Filter for json files
    json_files = [file for file in files if file.endswith('.json')]

    # Process all json files
    for json_file in json_files:
        json_file_path = os.path.join(input_folder_path, json_file)
        characterization_data = get_characterization(json_file_path)

        if characterization_data is not None:
            output_file_path = os.path.join(output_folder_path, f'characterization_{json_file}')
            
            with open(output_file_path, 'w') as output_file:
                json.dump(characterization_data, output_file)
                print(f'Characterization data for {json_file} has been written to {output_file_path}')


input_folder_path = '/Users/defnecirci/Desktop/nlp-for-materials/evaluation/untitledfolder'  # replace with your input folder path
output_folder_path = '/Users/defnecirci/Desktop/nlp-for-materials/evaluation/characterization_sample_jsons'  # replace with your output folder path
process_all_json_in_folder(input_folder_path, output_folder_path)
