### Data-Cleaning

import pandas as pd

## Handling Duplicates

# Create a sample dataset with duplicate values
data = {'A': ['foo', 'bar', 'foo', 'baz', 'qux', 'baz', 'foo'],
        'B': [1, 2, 3, 4, 5, 6, 7],
        'C': [10, 20, 30, 40, 50, 60, 70]}
df = pd.DataFrame(data)

# Print the original dataframe
print('Original dataframe:')
print(df)


# Drop duplicates
df.drop_duplicates(subset=['A'], inplace=True)
print('\nDataframe after dropping duplicates:')
print(df)


# Aggregate duplicates
agg_df = df.groupby(['A']).mean()
print('\nDataframe after aggregating duplicates:')
print(agg_df)


# Keep the first occurence
first_df = df.drop_duplicates(subset=['A'], keep='first')
print('\nDataframe after keeping the first occurence:')
print(first_df)


# Keep the last occurence
last_df = df.drop_duplicates(subset=['A'], keep='last')
print('\nDataframe after keeping the last occurence:')
print(last_df)


# Mark duplicates
df['duplicate'] = df.duplicated(subset=['A'])
print('\nDataframe after marking duplicates:')
print(df['duplicate'])


