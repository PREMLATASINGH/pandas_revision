import numpy as np
import pandas as pd
data={
    "product":["laptop","phone","chair","table","laptop",'airpot','table'],
    "category":["tech","tech","furniture","furniture","tech",'tech',"furniture"],
    "quantity":[1,2,3,1,2,7,4],
    "price":[1200,800,150,300,1200,500,675],
    "sales":[900,500,100,200,900,700,800],
    "region":["east","west","east","south","west","east","west"],
    "date":['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-01','2024-01-05','2024-01-06']
}
df=pd.DataFrame(data)
print(df)
total_sales=df['sales'].sum()
print('total_sales:',total_sales)
print(df.columns)
print(df.info())
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.fillna(0))
print(df.describe())
print(type(df))
print(df.drop_duplicates('date'))
df = df.rename(columns={'sales': 'total_sales'})
df1=df.groupby('product')['total_sales'].sum()
print(df1)
df2=df.groupby('region')['total_sales'].sum()
print(df2)
df3=df.groupby('category')['total_sales'].sum()
print(df3)
df4=df.groupby(['region','category'])['total_sales'].sum()
print(df4)
df5=df['total_sales'].sort_values(ascending=True)
print(df5)
df6=df['product'].unique()
print(df6)
df7=df.sort_values(by='product').head(5)
print(df7)
df8=df.sort_values(by='category').head()
print(df8)

