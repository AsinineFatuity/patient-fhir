import json 

with open('sample_patient.json', 'r') as file:
    patient_data = json.load(file)

print(patient_data)