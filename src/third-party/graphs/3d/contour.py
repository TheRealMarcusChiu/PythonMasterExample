import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-6, 6, 120)
y = np.linspace(-6, 6, 120)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
num_contours = 50
ax.contour3D(X, Y, Z, num_contours)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# elevation of 60 degrees (that is, 60 degrees above the x-y plane)
elevation = 60
# azimuth of 35 degrees (that is, rotated 35 degrees counter-clockwise about the z-axis)
azimuth = 35
ax.view_init(elevation, azimuth)

plt.show()
