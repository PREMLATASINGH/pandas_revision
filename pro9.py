import numpy as np
import pandas as pd
data={
    'product_id':[101,102,103,104,105],
    'product_name':['Laptop','Smartphone','Tablet','Headphones','Smartwatch'],  
    'category':['Electronics','Electronics','Electronics','Accessories','Electronics'],
    'price':[1000,800,600,150,200],
    'stock':[50,100,80,200,150],
    'release_date':['2021-01-10','2020-05-15','2021-08-20','2019-11-05','2020-09-30']
}
df=pd.DataFrame(data)
print(df)
df.loc[2,'price']=np.nan
print(df)
print(df.dropna())
print(df.fillna(df['price'].mean()))
print(df['price'].isnull().sum())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.fillna(0, inplace=True))
print(df.isnull().sum())
print(df.groupby('category')['price'].mean())
print(df.groupby('category')['stock'].sum())
print(df.sort_index(ascending=False))
print(df.sort_values(by='price', ascending=True))
print(df.sort_values(by=['category','price'], ascending=[True,False]))
print(df[df['price']>500])
print(df.columns)
print(df.index)
print(df.describe())
print(df.info())
print(df['release_date'].max())

