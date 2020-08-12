import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('Original array is: \n', a, '\n')

print('iterated: ')
for x in np.nditer(a):
    print(x, end=", ")
print('\n')

print('iterated (order=\'C\'): ')
for x in np.nditer(a, order='C'):
    print(x, end=", ")
print('\n')

print('iterated (order=\'F\'): ')
for x in np.nditer(a, order='F'):
    print(x, end=", ")
print('\n')

a = a.copy(order='F')
print('iterated of copy (order=\'F\'): ')
for x in np.nditer(a):
    print(x, end=", ")
print('\n')

print('modified array is: ')
print(2 * a)
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('\nModified array is: ')
print(a)

