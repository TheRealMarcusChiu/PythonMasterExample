import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-6, 6, 60)
y = np.linspace(-6, 6, 60)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

##################################
# METHOD 1 - Using WireFrame API #
##################################
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
ax.set_title('wireframe')
plt.show()

###################################################
# METHOD 2 - Using Surface API With No Face Color #
###################################################
# Normalize to [0,1]
norm = plt.Normalize(Z.min(), Z.max())
colors = cm.viridis(norm(Z))
rcount, ccount, _ = colors.shape

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rcount=rcount, ccount=ccount, facecolors=colors, shade=False)
surf.set_facecolor((0, 0, 0, 0))
plt.show()
