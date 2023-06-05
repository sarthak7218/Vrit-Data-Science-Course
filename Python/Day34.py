## Data Normalization

import pandas as pd
import numpy as np

# Crate a dummy dataset
data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'value': [10, 20, 30, 40, 50]
})


# Perform min-max normaliztion
data['value_norm_minmax'] = (data['value'] - data['value'].min()) / (data['value'].max() - data['value'].min())


# Perform z-score normalization
data['value_norm_zscore'] = (data['value'] - data['value'].mean()) / data['value'].std()


# PErform log normalization
data['value_norm_log'] = np.log(data['value'])


# Perform power normalization with a = 0.5
data['value_norm_power'] = np.sign(data['value']) * np.power(np.abs(data['value']), 0.5)


# Print the data resulting DataFrame
print(data)


### Handling-Missing-Values

# Create a dataframe with missing values
df = pd.DataFrame({
    'col1': [1, 2, np.nan, 4, 5],
    'col2' : [6, np.nan, 8, 9, 10],
    'col3': [11, 12, 13, np.nan, 15]
})

# Display the DataFrame
print("Original data\n", df)

# List-wise deletion
new_df = df.dropna()
print("\nDataFrame after list-wise deletion:\n", new_df)

# Pair-wise deletion
new_df = df.dropna(subset=['col1', 'col2'])
print("\nDataFrame after pair-wise deletion:\n", new_df)

# Column-wise deletion
new_df = df.dropna(axis=1)
print("\nDataFrame after column-wise deletion:\n", new_df)


