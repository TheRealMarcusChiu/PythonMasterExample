import numpy as np

a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print(a)

axis = np.ndim(a) - 1
print('\n', np.sort(a, axis=axis, kind='quicksort'))
print('\n', np.sort(a, axis=axis, kind='mergesort'))
print('\n', np.sort(a, axis=axis, kind='heapsort'))
