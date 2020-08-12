import numpy as np

a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])

print('\nApplying nonzero() function:')
indices = np.nonzero(a)
print(indices)
print(a[indices])

print('\nApplying where() function:')
indices = np.where(a > 40)
print(indices)
print(a[indices])

# define a condition
condition = np.mod(a, 20) == 0
print('\nElement-wise value of condition')
print(condition)
print('Extract elements using condition')
print(np.extract(condition, a))
