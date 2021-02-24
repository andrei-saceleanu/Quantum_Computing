from qiskit import QuantumCircuit,execute,Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


#n=8
#qc_output=QuantumCircuit(n,n)
#for i in range(n):
#	qc_output.measure(i,i)
#counts = execute(qc_output,Aer.get_backend('qasm_simulator')).result().get_counts()
#qc_output.draw(output='mpl')
#plt.show()


qc=QuantumCircuit(2,2)
qc.x(0)
qc.cnot(0,1)
qc.measure(0,0)
qc.measure(1,1)
counts = execute(qc,Aer.get_backend('qasm_simulator')).result().get_counts()
plot_histogram(counts)
plt.show()

