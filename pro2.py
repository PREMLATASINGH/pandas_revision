import numpy as np
import pandas as pd
data={
     "product":["laptop","phone","chair","table","laptop",'airpot','table','chair'],
    "category":["tech","tech","furniture","furniture","tech",'tech',"furniture","furniture"],
    "quantity":[1,2,3,1,2,7,4,5],
    "price":[1200,800,150,300,1200,500,675,150],
    "sales":[900,500,100,200,900,700,800,890],
    "region":["east","west","east","south","west","east","west","east"],
    "date":['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-01','2024-01-05','2024-01-06','2024-01-07']
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
print(df.drop_duplicates('date'))
print(df.shape)
print(df.columns)
print(df.describe())
df1=df['sales'].unique()
print(df1)
df2=df["sales"].sort_values(ascending=True)
print(df2)
df3=df['price'].sort_values(ascending=True)
print(df3)
df4=df.groupby('product')['sales'].sum()
print(df4)
df['total_sales']=df['price']*df['quantity']
print(df)
df=df.drop_duplicates(subset='date')
print(df)
df['price']=df['price'].fillna(df['price'].mean())
print(df)
df4=df[df["price"]>500]
print(df4)
df5=df[(df['region']=='east') & (df['price']>500)]
print(df5)
df6=df.groupby('region')['total_sales'].sum()
print(df6)
df7=df.sort_values(by='total_sales', ascending=False).head(5)
print(df7)
df8=df.sort_values(by='total_sales', ascending=True).tail(3)
print(df8)
df9=pd.pivot_table(
    df,
    values='total_sales',
    index='region',
    columns='category',
    aggfunc='sum'   
)
print(df9)
print(df['total_sales'].sum())
print(df['total_sales'].mean())
print(df['total_sales'].min())
print(df['total_sales'].max())
df['high_sales']=df['total_sales'].apply(lambda x: 'High' if x > 1000 else 'Low' )
print(df)
df10=pd.DataFrame({
    'product':['laptop','phone','chair','table','airpot'],
    'discount':[0.1,0.2,0.15,0.05,0.25]
})
print(df.merge(df10, on='product'))
print(df.merge(df10, on='product', how='left'))