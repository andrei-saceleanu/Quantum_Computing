from qiskit import QuantumCircuit,execute,Aer
from qiskit.visualization import plot_histogram,plot_bloch_multivector
import matplotlib.pyplot as plt
from math import sqrt,pi

backend=Aer.get_backend('statevector_simulator')
qc=QuantumCircuit(1)
qc.h(0)
out=execute(qc,backend).result().get_statevector()
plot_bloch_multivector(out)
plt.show()
