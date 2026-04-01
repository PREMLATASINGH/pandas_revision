import numpy as np
import pandas as pd
data={
    'student':['raj','rani','ranu','raja','adu','uday'],
    'score':[70,80,87,67,99,99],
    'weight':[5,4.11,5,6,6,5.9]
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
df1=df.groupby('student')['score'].mean()
print(df1)
total_score=df['score'].sum()
print('total_score:',total_score)
total_weight=df['weight'].sum()
print('total_weight:',total_weight)
df2=df.groupby('weight')['score'].sum()
print(df2)
df3=df.groupby('student')['score'].idxmax()
print(df3)
df4=df['score']>80
print(df4)
df5=df['weight']>5
print(df5)
df6=df['student']=='raja'
print(df6)

