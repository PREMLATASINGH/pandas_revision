import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
df=pd.read_csv('netflix_titles.csv')
print(df.head())
print(df.info())
print(df.describe())