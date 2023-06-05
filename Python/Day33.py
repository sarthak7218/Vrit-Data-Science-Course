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


# Create a dummy dataset
data = pd.Dataframe({'id': [1, 2, 3, 4, 5],
                     'name': ['John', 'Jane', 'Bob', 'Alice', 'David'],
                     'age': [25, -31, 42, 19, 37],
                     'gender': ['M', 'F', 'M', 'M', 'F'],
                     'income': [50000, 70000, np.nan, '30000', 60000]})
                     
                     
# Identify incorrect data
incorrect_age = data[(data['age'] <=0) | (data['age'] > 100)]
incorrect_gender = data[~data['gender'].isin(['M', 'F'])]
incorrect_income = data[~data['income'].apply(lambda x: isinstance(x, (int, float)))]


# Delete incorrect data
data = data.drop(incorrect_age.index)
data = data.drop(incorrect_gender.index)
data = data.drop(incorrect_income.index)


# Display the cleaned dataset
print("\nDataset after handling Incorrect Values")
print(data)



### Handling Inconstient Data

# Create a dummy dataset
data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5]
    'country': ['USA', 'U.S.A', 'Unites States', 'Canada', 'Mexico']
    'date': ['2021-01-01', '01/01/2021', '2021-01-01', '01-01-2021']
})

# Define rules for resolving inconsistencies
country_code = {
    'USA': 'US',
    'United States': 'US',
    'U.S.A': 'US',
    'Canada': 'CA',
    'Mexico': 'MX'
}
print("Inconsistent Data")
print(data)

def parse_date(date_str):
    if '-' in date_str:
        return date_str
    elif '/' in date_str:
        parts = date_str.split('/')
        return f'{parts[2]}-{parts[0]}-{parts[1]}'
    else:
        parts = date_str.split('-')
        
    