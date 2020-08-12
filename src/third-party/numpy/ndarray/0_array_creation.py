import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=None, copy=True, order=None, subok=False, ndmin=0)
print(a.dtype)  # outputs int64 even thought it was explicitly set to None
print(a)
# other int types
a = np.array([1, 2, 3, 4, 5], dtype=np.int64)
a = np.array([1, 2, 3, 4, 5], dtype=np.int32)
a = np.array([1, 2, 3, 4, 5], dtype=np.int16)
a = np.array([1, 2, 3, 4, 5], dtype=np.int8)
a = np.array([1, 2, 3, 4, 5], dtype=complex)
print(a)
# order
a = np.array([1, 2, 3, 4, 5], order='C')  # C-style row-major array
a = np.array([1, 2, 3, 4, 5], order='F')  # Fortran-style column-major array
# minimum dimensions
a = np.array([1, 2, 3, 4, 5], ndmin=7)
print(a)

shape = [1, 3]
x = np.empty(shape, dtype=int)
print('empty: ', x)
x = np.zeros(shape, dtype=int)
print('zeros: ', x)
x = np.ones(shape, dtype=int)
print('ones: ', x)
x = np.zeros(shape, dtype=[('x', np.complex), ('y', int)])
print('custom dtype: ', x)
x = [[1, 2, 3], [4, 5]]
a = np.asarray(x)
print('asarray: ', a)
a = np.frombuffer(b'Hello World', dtype='S1', count=-1)
print('frombuffer: ', a)
x = np.arange(start=5, stop=10, step=0.5)
print('arange: ', x)
x = np.linspace(start=9, stop=10, num=11)
print('linspace: ', x)
x = np.logspace(1.0, 2.0, num=5)
print('logspace: ', x)
