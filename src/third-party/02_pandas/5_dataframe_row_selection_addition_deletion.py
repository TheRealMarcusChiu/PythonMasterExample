import pandas as pd

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

# ROW SELECTION
print('\nROW SELECTION')
print(df.loc['b'])
# print(df.iloc[2]) # integer selection

# ROW SLICE
print('\nROW SLICE')
print(df[2:4])

# ROW ADDITION
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['one', 'two'])
df = df.append(df2)
print('\nROW ADDITION')
print(df)

# ROW DELETION
df = df.drop('a')
print('\nROW DELETION')
print(df)
