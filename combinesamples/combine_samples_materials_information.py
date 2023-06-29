import json
import glob
import os

# Specify the directory containing the folders
directory = '/Users/defnecirci/Desktop/nlp-for-materials/combinesamples/articlejsons'

# List all folders in the directory
folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]

# Loop through each folder
for folder in folders:
    print("folder: ", folder)
    # Create a separate output folder for each folder
    output_folder = os.path.join("/Users/defnecirci/Desktop/nlp-for-materials/combinesamples/output", folder + '_output')
    os.makedirs(output_folder, exist_ok=True)

    # Set the current working directory to the folder
    folder_path = os.path.join(directory, folder)
    os.chdir(folder_path)

    # List all JSON files in the folder
    json_files = glob.glob('*.json')

    # Initialize dictionaries to store the extracted information
    matrix_info = {
        "Chemical name": set(),
        "Abbreviation": set()
    }
    filler_info = {
        "Filler name": set(),
        "Filler abbreviation": set(),
        "Particle diameter": set()
    }
    filler_comp_info = {
        "mass fraction": set(),
        "volume fraction": set()
    }
    pst_info = {
        "PST chemical name": set(),
        "PST abbreviation": set()
    }

    # Loop through each JSON file
    for file_path in json_files:
        # Load the JSON data
        with open(file_path) as file:
            data = json.load(file)

        # Extract the required information if available
        polymer_nanocomposite = data.get('PolymerNanocomposite', {})
        if isinstance(polymer_nanocomposite, dict):
            materials = polymer_nanocomposite.get('MATERIALS', {})
            if isinstance(materials, dict):
                matrix_component = materials.get('Matrix', {}).get('MatrixComponent', {})
                if isinstance(matrix_component, dict):
                    matrix_info["Chemical name"].add(matrix_component.get('ChemicalName', ''))
                    matrix_info["Abbreviation"].add(matrix_component.get('Abbreviation', ''))


                filler = materials.get('Filler', {})

                if isinstance(filler, dict):
                    filler_component = filler.get('FillerComponent', {})
                    if isinstance(filler_component, dict):
                        filler_info["Filler name"].add(filler_component.get('ChemicalName', ''))
                        filler_info["Filler abbreviation"].add(filler_component.get('Abbreviation', ''))

                        spherical_particle_diameter = filler_component.get('SphericalParticleDiameter')
                        if isinstance(spherical_particle_diameter, dict):
                            filler_info["Particle diameter"].add(spherical_particle_diameter.get('value', ''))

                        filler_comp = filler_component.get('FillerComponentInComposite', {})
                        if isinstance(filler_comp, dict):
                            filler_comp_info["mass fraction"].add(filler_comp.get('mass', ''))
                            filler_comp_info["volume fraction"].add(filler_comp.get('volume', ''))


                        particle_surface_treatment = filler_component.get('ParticleSurfaceTreatment', [])
                        if isinstance(particle_surface_treatment, list):
                            pst_info["PST chemical name"].update([item.get('ChemicalName', '') for item in particle_surface_treatment])
                            pst_info["PST abbreviation"].update([item.get('Abbreviation', '') for item in particle_surface_treatment])


    # Convert sets to lists and remove empty strings
    matrix_info = {key: list(filter(None, value)) for key, value in matrix_info.items()}
    filler_info = {key: list(filter(None, value)) for key, value in filler_info.items()}
    filler_comp_info = {key: list(filter(None, value)) for key, value in filler_comp_info.items()}
    pst_info = {key: list(filter(None, value)) for key, value in pst_info.items()}


    # Construct the output dictionary
    output = {
        "Matrix": matrix_info,
        "Filler": filler_info,
        "Filler Composition": filler_comp_info,
        "Particle Surface Treatment (PST)": pst_info
    }
    # Print the output
    output_file = os.path.join(output_folder, folder + '.json')
    with open(output_file, 'w') as file:
        json.dump(output, file, indent=4)
