import pandas as pd

data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print('\nLIST')
print(df)

data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data)
print('\nDICT')
print(df)

df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print('\nDICT WITH INDEX')
print(df)

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print('\nLIST of DICT')
print(df)

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print('\nWith two column indices, values same as dictionary keys')
print(df1)
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print('\nWith two column indices with one index with other name')
print(df2)

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print('\nDICT of SERIES')
print(df)
