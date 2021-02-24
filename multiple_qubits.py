from qiskit import QuantumCircuit,Aer,execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from math import sqrt,pi

#qc=QuantumCircuit(2)
#qc.h(0)
#qc.x(1)
#qc.draw(output='mpl')
#plt.show()
#backend=Aer.get_backend('unitary_simulator')
#unitary=execute(qc,backend).result().get_unitary()
#print(unitary)


qc=QuantumCircuit(2)
qc.h(0)
qc.x(1)
qc.cx(0,1)
backend=Aer.get_backend('statevector_simulator')
results=execute(qc,backend).result().get_counts()
plot_histogram(results)
plt.show()
