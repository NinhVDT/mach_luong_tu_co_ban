import json
from qiskit_ibm_runtime import QiskitRuntimeService

# Read api token from config.json file
with open('config.json', 'r') as file:
    data = json.load(file)

# Register based on the api token provided
QiskitRuntimeService.save_account(channel="ibm_quantum", token=data["api_token"], overwrite=True)
print("Success!")