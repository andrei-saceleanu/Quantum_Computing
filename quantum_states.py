from qiskit import QuantumCircuit,execute,Aer
from qiskit.visualization import plot_histogram,plot_bloch_vector
import matplotlib.pyplot as plt
from math import sqrt,pi

backend = Aer.get_backend('statevector_simulator')
initial_state=[1/sqrt(3),-sqrt(2/3)]
qc=QuantumCircuit(1)
qc.initialize(initial_state,0)
state=execute(qc,backend).result().get_statevector()
print(state)
#counts=execute(qc,backend).result().get_counts()
#plot_histogram(counts)
#plt.show()
qc.measure_all()
state=execute(qc,backend).result().get_statevector()
print(state)
plot_bloch_vector([1,pi/2,0],coord_type='spherical')
plt.show()
