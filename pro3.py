import numpy as np
import pandas as pd
data={
    'employee_id':[1,2,3,4,5],
    'name':['Alice','Bob','Charlie','David','Eve'],
    'department':['HR','IT','Finance','IT','HR'],
    'salary':[50000,60000,55000,70000,52000],
    'join_date':['2020-01-15','2019-03-10','2021-06-20','2018-11-05','2020-09-30']
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
print(df.drop_duplicates('department'))
print(df.shape)
print(df.columns)
print(df.describe())
df1=df['salary'].unique()
print(df1)
df2=df['department'].unique()
print(df2)
df3=df['salary'].sort_values(ascending=False)
print(df3)
df4=df['department'].value_counts()
print(df4)
df['annual_salary']=df['salary']*12
print(df)
df5=df['department'].sort_values(ascending=True)
print(df5)
df6=df.groupby('department')['annual_salary'].sum()
print(df6)
df7=df.sort_values(by='annual_salary', ascending=False).head(3)
print(df7)
df8=df.sort_values(by='annual_salary', ascending=True).tail(2)
print(df8)
df9=pd.pivot_table(
    df,
    values='annual_salary',
    index='department',
    columns='name',
    aggfunc='sum'
)
print(df9)
print(df['annual_salary'].sum())
print(df['annual_salary'].mean())
print(df['annual_salary'].min())
print(df['annual_salary'].max())
df['salary_level']=df['annual_salary'].apply(lambda x: 'High' if x > 600000 else 'Low')
print(df)
df10=pd.DataFrame({
    'department':['HR','IT','Finance'],
    'budget':[200000,300000,250000]
})
print(df.merge(df10, on='department'))
print(df.merge(df10, on='department', how='left'))
print(df.merge(df10, on='department', how='right'))
print(df.merge(df10, on='department', how='outer'))
print(df.groupby('department')['annual_salary'].sum().reset_index())  
print(df.groupby('department')['annual_salary'].mean().reset_index())  
print(df.groupby('department')['annual_salary'].min().reset_index())