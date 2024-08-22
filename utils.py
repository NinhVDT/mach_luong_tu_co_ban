# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
import pickle
# import pickle5
from qiskit.providers.aer.noise import NoiseModel
# from qiskit.compiler import transpile, assemble
# from qiskit.tools.jupyter import *
# from qiskit.visualization import *
# import qiskit.quantum_info as qi
# Loading your IBM Q account(s)
# provider = IBMQ.load_account()



def save_backend(backend_name):
    """
    Saves the coupling map and noise model using pickle. 
    Whenever the replicated backend needs to be invoked, use picle to load the moise model and coupling map. 
    """
    # Import the NoiseModel
    # Obtain the backend to simulate
    backend = provider.get_backend(backend_name)
    # Create the noise model based on the backend properties
    noise_model = NoiseModel.from_backend(backend)
    with open(f'noise_{backend_name}.pkl', 'wb') as handle:
        b = pickle.dump(noise_model, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Get coupling map from backend
    coupling_map = backend.configuration().coupling_map
    with open(f'coupling_{backend_name}.pkl', 'wb') as handle:
        b = pickle.dump(coupling_map, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Get basis gates from noise model
    basis_gates = noise_model.basis_gates

    return coupling_map, basis_gates, noise_model
    
def load_backend(backend_name):
    """
    Loads the saved coupling map and noise model using pickle
    """
    # Load the noise model
    with open(f'noise_{backend_name}.pkl', 'rb') as handle:
        noise_model = pickle.load(handle)

    # Load the coupling map
    with open(f'coupling_{backend_name}.pkl', 'rb') as handle:
        coupling_map = pickle.load(handle)

    # Get basis gates from noise model
    basis_gates = noise_model.basis_gates

    return coupling_map, basis_gates, noise_model