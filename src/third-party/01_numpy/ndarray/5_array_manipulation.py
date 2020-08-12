import numpy as np

a = np.arange(8).reshape(2, 4)
print('The original array:')
print(a)

print('After applying the flat function:')
iterr = a.flat  # returns a 1-D iterator over the array
print(iterr[5])

# https://www.tutorialspoint.com/numpy/numpy_array_manipulation.htm
