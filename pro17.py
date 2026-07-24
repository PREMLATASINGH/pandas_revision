import numpy as np
import pandas as pd
df = pd.read_csv("employees_1000.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df['salary'].mean())
print(df['salary'].median())
print(df['salary'].mode())
print(df.isnull().sum())