import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data={
    'order_id':[1,2,3,4,5,6,7,8],
    'region':['North','South','East','West','North','South','East','West'],
    'sales':[100,150,200,250,300,350,400,450],
    'product':['A','B','C','D','A','B','C','D'],
    'profit':[10,15,20,25,30,35,40,45]
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
df.loc[2,'sales']=np.nan
print(df)
print(df.isnull())
df1=df['sales'].fillna(df['sales'].mean(),inplace=True)
print(df1)
df=df.drop_duplicates()
print(df)
df['revenue']=df['sales']+df['profit']
print(df)
df['profit_level']=df['profit'].apply(lambda x:'High' if x>30 else 'Low')
print(df)
high_sales=df[df['sales']>200]
print(high_sales)
df_sorted=df.sort_values(by='sales',ascending=False)
print(df_sorted)
region_sales=df.groupby('region')['sales'].sum()
print(region_sales)
prooduct_profit=df.groupby('product')['profit'].mean()
print(prooduct_profit)
sales_array=np.array(df['sales'])
print('total_sales:',np.sum(sales_array))
print('average_sales:',np.mean(sales_array))