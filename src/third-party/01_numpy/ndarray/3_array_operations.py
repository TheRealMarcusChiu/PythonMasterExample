import numpy as np

# ordinary operations
a = np.array([0, 0, 0])
b = np.array([1, 2, 3])
c = a + b
print(c)

# broadcasting
a = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20]])
b = np.array([1, 2, 3])
c = a + b
print(c)
