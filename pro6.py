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
print(df['age'].median())
print(df.groupby('gender')['purchase_amount'].sum())
print(df.groupby('gender')['purchase_amount'].mean())
print(df.sort_values(by='purchase_amount', ascending=False))
print(df['purchase_date'].value_counts())
print(df['age'].value_counts())
print([df.drop_duplicates('purchase_date')])
print(df['customer_name'].str.upper())
print(df['customer_name'].str.lower())
print(df['customer_name'].str.len())
print(df['customer_name'].str.contains('a'))
print(df.groupby('gender')['age'].mean())
print(df.groupby('gender')['age'].median())
print(df.groupby('gender')['age'].sum())
print(df.sort_values(by='age', ascending=True))
print(df.sort_values(by='age', ascending=False))
print(df['purchase_amount'].describe())
print(df['age'].dropna().describe())
df1=pd.DataFrame({'customer_id':[11,12],
                  'customer_name':['Karl','Liam'],
                  'age':[28,32],
                  'gender':['M','M'],
                  'purchase_amount':[200,300],
                  'purchase_date':['2024-01-11','2024-01-12']
})
print(df1)

