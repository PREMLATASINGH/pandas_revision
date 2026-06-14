import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
df=pd.read_csv('netflix_titles.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.fillna(0))
print(df['type'].value_counts())
print(df[df['type']=='Movie'])
print(df[df['type']=='TV Show'])
print(df.columns)
print(df['release_year'].unique())
print(df.groupby('release_year')['type'].count())