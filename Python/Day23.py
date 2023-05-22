##Data-Manupulation

import pandas as pd

data = {'name': ['alice', 'Bob', 'Charlie', 'Jane'], 'age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

print(df.head())

df.iloc[0, 1]
print(df.head())

print(df.age)

df['height'] = [165, 180, 175, 144]
print(df.head())

df['test'] = [2, 3, 4,  '']
print(df.head())

print(df.isna())

df['test'] = [1, 2, 3, 4]
print(df.head())

df['gender'] = 'Male'
print(df.head())

print(df.isna())

print(df.isna().sum())

df.gender.fillna('Female', inplace=True)
print(df.head())


print(df.head())

df.dropna(inplace=True)
print(df.head())

df.drop('gender', axis=1)
print(df.head())

print(df.reset_index().drop('index', axis=1))

print(df.columns)

col_mapper = {'name': 'Name', 'age':'Age', 'gender':'Gender'}
print(df.rename(columns=col_mapper))

def double(x):
    return x * 2

print(df['age'].apply(double))

grouped_df = df. groupby('gender')
print(grouped_df)

print(grouped_df.agg({"age":"mean"}))

                             


