import numpy as np

# array attributes
a = np.array([[[1, 2, 3], [4, 5, 6]],
              [[1, 2, 3], [4, 5, 6]],
              [[1, 2, 3], [4, 5, 6]],
              [[1, 2, 3], [4, 5, 6]]])
print('shape: ', a.shape)
print('ndim: ', a.ndim)
print('dtype: ', np.dtype(a[0, 0, 0]))
print('itemsize (bytes): ', a.itemsize)