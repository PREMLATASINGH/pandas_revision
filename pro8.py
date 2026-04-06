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