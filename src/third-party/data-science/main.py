import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# construct population
population = np.random.randint(0, 500, size=100)

# # sample population of size 30
# sample = np.random.choice(population, size=30)
# print('sample mean: ', sample.mean())
# print('sample std: ', sample.std())
#
# # estimated standard error for the sample mean
# print('estimated SE: ', sample.std()/(30 ** 0.5))

# construct the simulated sampling distribution
sample_size = 30
sample_means = []
for _ in range(100000):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(sample.mean())

# the theoretical mean and simulated mean of the sample distribution
print('theoretical mean: ', population.mean())
print('estimated mean:   ', np.mean(sample_means))
# the theoretical standard error and estimated standard error of the sampling distribution
print('theoretical standard error: ', population.std() / (sample_size ** 0.5))
print('estimated standard error:   ', np.std(sample_means))

plt.hist(sample_means)
plt.show()
