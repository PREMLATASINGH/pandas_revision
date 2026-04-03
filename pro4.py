import pandas as pd
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

