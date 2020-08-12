import pandas as pd
import numpy as np


def adder(ele1, ele2):
    return ele1 + ele2


rand = np.random.randn(5, 3)  # 5x3 matrix of random
df = pd.DataFrame(rand, columns=['col1', 'col2', 'col3'], index=['a', 'b', 'c', 'd', 'e'])
print(df)
print('\nPIPE adder (add 5 to every entry)')
print(df.pipe(adder, 5))
print('\nAPPLY np.mean (column wise)')
print(df.apply(np.mean, axis=0))  # col wise
print('\nAPPLY np.mean (row wise)')
print(df.apply(np.mean, axis=1))  # row wise

print('\nAPPLY lambda')
print(df.apply(lambda x: x.max() - x.min()))
print(df['col1'].max() - df['col1'].min())
print(df['col2'].max() - df['col2'].min())
print(df['col3'].max() - df['col3'].min())


# INDIVIDUAL ELEMENTS
print('\nMAP lambda on single column')
print(df['col1'].map(lambda x: x * 100))
print('\nMAP lambda on ALL elements')
print(df.applymap(lambda x: x * 100))
