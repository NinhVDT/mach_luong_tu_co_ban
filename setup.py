from qiskit_ibm_runtime import QiskitRuntimeService
# IBM Quantum channel; set to default 
 
QiskitRuntimeService.save_account(channel="ibm_quantum", token="e57284b24d2033f21800735dd8544e995c549ec89e5d10f1f60ba9eedb895eacb4653df2be519cd194c1d12653df97aa1789ca8d74b1eeb7906c9116b277cabf", overwrite=True)
print("Success!")