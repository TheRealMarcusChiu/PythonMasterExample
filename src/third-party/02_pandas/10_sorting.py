import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])
print(unsorted_df)

# SORT BY INDEX/LABEL
print('\nSORT - ROW LABEL ASCENDING')
print(unsorted_df.sort_index())
print('\nSORT - ROW LABEL DESCENDING')
print(unsorted_df.sort_index(ascending=False))
print('\nSORT - COL LABEL ASCENDING')
print(unsorted_df.sort_index(axis=1))

# SORT BY VALUE
print('\nSORT - COL1 VALUE ASCENDING')
print(unsorted_df.sort_values(by='col1'))
print('\nSORT - COL1 VALUE then COL2 - ASCENDING')
print(unsorted_df.sort_values(by=['col1', 'col2']))

# SORT ALGORITHM
print('\nSORT - MERGESORT')
print(unsorted_df.sort_values(by='col1', kind='mergesort'))
print('\nSORT - QUICKSORT')
print(unsorted_df.sort_values(by='col1', kind='quicksort'))