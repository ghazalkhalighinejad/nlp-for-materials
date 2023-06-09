import json
from sklearn.metrics import precision_score, recall_score, f1_score

text1 = '''
Characterization: {
    "Microscopy": {
        "Transmission electron microscopy": {
            "EquipmentUsed": "JEOL CX100",
            "Voltage": "100 kV"
        },
        "Scanning electron microscopy": {},
        "Atomic force microscopy": {},
        "Optical microscopy": {}
    },
    "Spectroscopy": {
        "Fourier transform infrared spectroscopy": {},
        "Xray photoelectron spectroscopy": {},
        "Nuclear magnetic resonance": {},
        "Raman spectroscopy": {},
        "Dielectric and impedance spectroscopy analysis": {}
    },
    "Thermochemical": {
        "Differential scanning calorimetry": {},
        "Thermogravimetric analysis": {
            "EquipmentUsed": "TA Instruments SDT 2960 Simultaneous DTA-TGA",
            "Atmosphere": "Nitrogen",
            "TemperatureRange": "Room temperature to 700°C"
        },
        "Dynamic mechanical analysis": {
            "EquipmentUsed": "TA Instruments DMA 2980 Dynamic Mechanical Analyzer",
            "Atmosphere": "Nitrogen",
            "TemperatureRange": "Room temperature to 150°C",
            "HeatingRate": "3°C/min",
            "Frequency": "1 Hz"
        }
    },
    "Scattering and diffraction": {
        "Xray diffraction and scattering": {}
    },
    "Others": {
        "Pulsed electro acoustic": {},
        "Rheometry": {},
        "Electrometry": {}
    }
}
'''

text2 = '''
{
    "Microscopy": {
        "transmission_electron_microscopy": {
            "EquipmentUsed": "JEOL CX100",
            "AcceleratingVoltage": {
                "value": "100",
                "unit": "kV"
            }
        },
        "scanning_electron_microscopy": {},
        "atomic_force_microscopy": {},
        "optical_microscopy": {}
    },
    "Spectroscopy": {
        "fourier_transform_infrared_spectroscopy": {},
        "xray_photoelectron_spectroscopy": {},
        "nuclear_magnetic_resonance": {},
        "raman_spectroscopy": {},
        "dielectric_and_impedance_spectroscopy_analysis": {}
    },
    "Thermochemical": {
        "differential_scanning_calorimetry": {},
        "thermogravimetric_analysis": {
            "Equipment": "TA Instruments SDT 2960 Simultaneous DTA-TGA"
        },
        "dynamic_mechanical_analysis": {
            "Equipment": "TA Instruments DMA 2980 Dynamic Mechanical Analyzer"
        }
    },
    "Scattering and diffraction": {
        "xray_diffraction_and_scattering": {}
    },
    "Others": {
        "pulsed_electro_acoustic": {},
        "rheometry": {},
        "electrometry": {}
    }
}
'''

# Convert the strings into Python dictionaries using the json library
data1 = json.loads(text1)
data2 = json.loads(text2)

# Function to get all keys from the nested dictionary
def get_filled_keys(data, current_key='', keys=None):
    if keys is None:
        keys = []
    for key, value in data.items():
        new_key = current_key + '.' + key if current_key else key
        if isinstance(value, dict):
            if value:  # Check if the dictionary is not empty
                keys.append(new_key)
                get_filled_keys(value, new_key, keys)
        else:
            keys.append(new_key)
    return keys

keys1 = get_filled_keys(data1)
keys2 = get_filled_keys(data2)

# Create binary lists indicating whether a key from text1 is present in text2, and vice versa
keys1_in_keys2 = [key in keys2 for key in keys1]
keys2_in_keys1 = [key in keys1 for key in keys2]

# Calculate precision, recall and f1 score
precision = precision_score(keys1_in_keys2, keys2_in_keys1)
recall = recall_score(keys1_in_keys2, keys2_in_keys1)
f1 = f1_score(keys1_in_keys2, keys2_in_keys1)

print('Precision: ', precision)
print('Recall: ', recall)
print('F1 Score: ', f1)
