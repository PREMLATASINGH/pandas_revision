import numpy as np
import pandas as pd
data={
    'student':['raj','rani','ranu','raja'],
    'score':[70,80,87,67]
}
df=pd.DataFrame(data)
print(df)
print(df.shape)
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())
print(df.columns)
print(df.isnull().sum())
print(df.fillna(0))
df1=df.groupby('student')['score'].sum()
print(df1)
total_score=df['score'].sum()
print('total_score:',total_score)
df2=df.groupby('student')['total_score'].sum()
print(df2)