import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Data={
    'order_id':[1,2,3,4,5,5],
    'product':['laptop','phone','tablet','laptop','phone','phone'],
    'region':['east','west','east','south','west','west'],
    'quantity':[1,2,1,3,2,2],
    'price':[1200,800,1200,500,300,300],
    'sales':[1000,500,None,1200,600,600]
    }
df=pd.DataFrame(Data)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
print(df.drop_duplicates('order_id'))
print(df.drop_duplicates('product'))
print(df.fillna(df['sales'].mean(), inplace=True))
df2=df.copy()
df2['tax']=df2['sales']*0.1
print(df2)
df['total_sales']=df['price']*df['quantity']
print(df)
df3=df[df['total_sales']>1000]
print(df3)
df4=df[(df['region']=='east') & (df['total_sales']>1000)]
print(df4)
df5=df.groupby('region')['total_sales'].sum()
print(df5)
df6=df.sort_values(by='total_sales', ascending=False).head(3)
print(df6)
df7=df.groupby('product')['total_sales'].mean()
print(df7)
df8=df.sort_values(by='total_sales', ascending=True).tail(2)
print(df8)
df9=pd.pivot_table(
    df,
    values='total_sales',
    index='region',
    columns='product',
    aggfunc='sum'
)
print(df9)
merged_df=pd.merge(df, df2[['order_id','tax']], on='order_id', how='outer')
print(merged_df)
df10=df.groupby('region')['total_sales'].sum().reset_index()
print(df10)
df11=df.groupby('product')['total_sales'].mean().reset_index()
print(df11)
df12=df['total_sales'].mean()
print(df12)
df13=df[df['total_sales']>df12]
print(df13)
df14=df[df['total_sales']<df12] 
print(df14)
print(df['total_sales'].describe())
print(df['total_sales'].value_counts())
print(df['total_sales'].unique())
print(df['total_sales'].nunique())
print(df['total_sales'].min())
df.loc[2,'total_sales']=np.nan
print(df)
print(df.isnull())
print(df.fillna(0))
plt.plot(df['region'],df['total_sales'])
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Total Sales by Region')
plt.show()
plt.bar(df['region'],df['total_sales'])
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Total Sales by Region')
plt.show()
plt.scatter(df['region'],df['total_sales'])
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Total Sales by Region')
plt.show()