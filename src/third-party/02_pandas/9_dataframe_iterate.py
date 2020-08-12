import pandas as pd
import numpy as np

# ITER IS NOT MEANT FOR WRITING JUST READING

N = 2
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N - 1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=N).tolist()
})

# ITERATE COLUMNS
print('\nITER COLUMNS')
for col in df:
    print(col)

# ITERATE ROWS
# - iteritems: to iterate over the (key,value) pairs
# - iterrows: iterate over the rows as (index,series) pairs
# - itertuples: iterate over the rows as namedtuples

# ITERITEMS
print('\nITER ROWS (ITERITEMS)')
for key, value in df.iteritems():
    print('KEY: ', key)
    print(value)

# ITERROWS
print('\nITER ROWS (ITERROWS)')
for row_index, row in df.iterrows():
    print('ROW INDEX: ', row_index)
    print(row)

# ITERTUPLES
print('\nITER ROWS (ITERTUPLES)')
for row in df.itertuples():
    print(row)

# ITER IS NOT MEANT FOR WRITING JUST READING
