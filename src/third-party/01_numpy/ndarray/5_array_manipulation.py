import numpy as np

a = np.arange(8).reshape(2, 2, 2)
print('\nThe original array:')
print(a)

a = a.reshape(2, 4)
print('\nAfter reshape(2, 4):')
print(a)

a = a.reshape(8)
print('\nAfter reshape(8):')
print(a)

print('\nAfter applying the flat function:')
iterr = a.flat  # returns a 1-D iterator over the array
print(iterr[5])

# https://www.tutorialspoint.com/numpy/numpy_array_manipulation.htm
