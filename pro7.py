import pandas as pd
data={
    'region':['North','South','East','West','North','South','East','West'],
    'sales':[100,150,200,250,300,350,400,450],
    'product':['A','B','C','D','A','B','C','D']
}
df=pd.DataFrame(data)
print(df)
print(df.groupby('region')['sales'].sum())
print(df.groupby('region')['sales'].mean())
print(df.groupby('region')['sales'].max())
pivot=pd.pivot_table(df,values='sales',index='region',columns='product',aggfunc='sum')
print(pivot)