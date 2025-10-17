import json 
from fhir.resources.patient import Patient
with open('sample_patient.json', 'r') as file:
    patient_data_dict = json.load(file)

validated_patient_data = Patient.model_validate(patient_data_dict)
print(validated_patient_data)
