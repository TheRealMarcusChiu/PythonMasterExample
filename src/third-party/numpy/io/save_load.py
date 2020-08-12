import numpy as np

# some binary format
a = np.array([1, 2, 3, 4, 5])
np.save('outfile', a)
b = np.load('outfile.npy')
print(b)

# text format
a = np.array([1, 2, 3, 4, 5], dtype=int)
np.savetxt('out.txt', a)
b = np.loadtxt('out.txt')
print(b)
