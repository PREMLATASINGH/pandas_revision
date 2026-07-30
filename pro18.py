import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('fact_sales.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
print(df.fillna(0, inplace=True))
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))