import numpy as np
import pandas as pd
data={'customer_id':[1,2,3,4,5,6,7,8,9,10],
      'customer_name':['Alice','Bob','Charlie','David','Eve','Frank','Grace','Heidi','Ivan','Judy'],
      'age':[25,30,35,40,45,None,55,60,65,70],
      'gender':['F','M','M','M','F','M','F','F','M','F'],
      'purchase_amount':[100,200,150,300,250,400,350,450,500,550],
      'purchase_date':['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-05','2024-01-06','2024-01-07','2024-01-07','2024-01-09','2024-01-10']
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
print(df.fillna(0))
print(df['age'].mean())
