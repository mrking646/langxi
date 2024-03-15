import pandas as pd

# Create two sample dataframes
df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': ['a', 'b', 'c'],
                    'C': ['foo', 'bar', 'baz']})

df2 = pd.DataFrame({'A': [1, 2, 4],
                    'B': ['a', 'b', 'd'],
                    'D': [10, 20, 30]})

# Merge the two dataframes with master preserving all rows
merged_df = pd.merge(df1, df2, on=['A', 'B'], how='left')

print(merged_df)