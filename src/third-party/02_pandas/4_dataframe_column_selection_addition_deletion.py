import pandas as pd

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

# COLUMN SELECTION
df = pd.DataFrame(d)
print('\nCOLUMN SELECTION')
print(df['one'])

# COLUMN ADDITION
df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
df['four'] = df['one'] + df['three']
print('\nCOLUMN ADDITION')
print(df)

# COLUMN DELETION
del df['one']
df.pop('two')
print('\nCOLUMN DELETION')
print(df)
