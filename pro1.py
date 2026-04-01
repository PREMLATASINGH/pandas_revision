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
df7=(df['score']>80)|((df['weight']>5)&(df['student']=='rani'))
print(df7)
print(type(df))
df8=df['student'].sort_values(ascending=True)
print(df8)
df9=df['weight'].sort_values(ascending=True)
print(df9)
df10=df['score'].sort_values(ascending=True)
print(df10)
df11=df['student'].unique()
print(df11)
df12=df['score'].unique()
print(df12)
df13=df['weight'].unique()
print(df13)
df14=df['student'].index[1:5]
print(df14)
df15=df['weight'].idxmax()
print(df15)
df16=df['weight'].index[0:5]
print(df16)
df17=df.sort_values(by='score').head(5)
print(df17)




