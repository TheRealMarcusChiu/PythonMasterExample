import numpy as np

print('NO COPY')
a = np.arange(6)
b = a
b.shape = 3, 2
print(a)
b[0, 0] = 22
print(a)

print('\nVIEW or SHALLOW COPY')
a = np.arange(6)
b = a.view()
b.shape = 3, 2
print(a)
b[0, 0] = 22
print(a)

print('\nDEEP COPY')
a = np.arange(6)
b = a.copy()
b.shape = 3, 2
print(a)
b[0, 0] = 22
print(a)
