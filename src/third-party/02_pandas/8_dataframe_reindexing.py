import pandas as pd
import numpy as np

# REINDEXING
N = 10
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(1, stop=N, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=N).tolist()
})
print('\nORIGINAL')
print(df)
df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])
print('\nREINDEX')
print(df_reindexed)

# REINDEX LIKE OTHER
print('\nREINDEX LIKE OTHER')
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['col1', 'col2', 'col_a', 'col_b'],
                   index=[0, 1, 2, 3, 4, 9, 10, 11, 12, 13])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['col1', 'col2', 'col3'])
print('\nDF1')
print(df1)
print('\nDF2')
print(df2)
print('\nDF1 REINDEX')
print(df1.reindex_like(df2))
print('\nDF1 REINDEX (FORWARD FILL)')
print(df1.reindex_like(df2, method='ffill'))
print('\nDF1 REINDEX (BACKWARD FILL)')
print(df1.reindex_like(df2, method='bfill'))
# print('\nDF1 REINDEX (NEAREST FILL)')
# print(df1.reindex_like(df2, method='nearest'))

# RENAMING INDICES & COLUMNS
print("\nAfter renaming the rows and columns:")
print(df1.rename(columns={'col1': 'c1', 'col2': 'c2'}, index={0: 'apple', 1: 'banana', 2: 'durian'}))
