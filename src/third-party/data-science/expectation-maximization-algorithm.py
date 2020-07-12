# example of a bimodal constructed from two gaussian processes
import numpy as np
from numpy import hstack
from numpy.random import normal
from matplotlib import pyplot
from sklearn.mixture import GaussianMixture

# generate a sample
X1 = normal(loc=20, scale=5, size=3000)
X2 = normal(loc=40, scale=5, size=7000)
X = hstack((X1, X2))

# # plot the histogram
pyplot.hist(X, bins=50, density=True)
pyplot.show()

# reshape into a table with one column
X = X.reshape((len(X), 1))
# fit model
model = GaussianMixture(n_components=2, init_params='kmeans')
model.fit(X)

print('means: ' + ''.join([line.strip() for line in str(model.means_)]))
print('covariances: ' + ''.join([line.strip() for line in str(model.covariances_)]))
print('converged: ' + ''.join([line.strip() for line in str(model.converged_)]))

# predict latent values
test = np.arange(0,60,0.5)
test = test.reshape(test.size, 1)
yhat = model.predict(test)
# check latent values
for i in range(0,120):
    print(str(yhat[i]) + ": " + str(test[i]))
