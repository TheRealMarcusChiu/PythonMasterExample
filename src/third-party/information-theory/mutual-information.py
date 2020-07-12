import numpy as np
from sklearn.metrics import mutual_info_score
from scipy.stats import chi2_contingency


# def calc_MI(x, y, bins):
#     c_xy = np.histogram2d(x, y, bins)[0]
#     g, p, dof, expected = chi2_contingency(c_xy, lambda_="log-likelihood")
#     mi = 0.5 * g / c_xy.sum()
#     return mi

def calc_MI(x, y, bins):
    c_xy = np.histogram2d(x, y, bins)[0]
    mi = mutual_info_score(None, None, contingency=c_xy)
    return mi

A = np.array([[ 1,  1,  128.23, -150.5, -5.4  ],
              [ 2,  2, 130.34, -130.1, -9.5  ],
              [ 3,  3,  120.11, -110.45,-1.12 ]])

bins = 5 # ?
n = A.shape[1]
matMI = np.zeros((n, n))

for ix in np.arange(n):
    for jx in np.arange(ix+1,n):
        matMI[ix,jx] = calc_MI(A[:,ix], A[:,jx], bins)

print(matMI)
