import pandas as pd
import matplotlib.pyplot as plt
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
print(pivot.fillna(0))
print(pivot.fillna(pivot.mean()))
print(pivot.fillna(pivot.median()))
pivot=pd.pivot_table(df,values='sales',index='region',aggfunc=['sum','mean','median'])
print(pivot)
pivot=pd.pivot_table(df,values='sales',index='region',columns='product',aggfunc='sum',fill_value=0)
print(pivot)
pivot=pd.pivot_table(df,values='sales',index='region',columns='product',aggfunc='sum',fill_value=0,margins=True)
print(pivot)
pivot.loc['North','A']=500
print(pivot)
pivot.loc['All','A']=pivot['A'].sum()
print(pivot)
pivot.iloc[0,0]=600
print(pivot)
pivot.iloc[-1,-1]=pivot.iloc[:-1,:-1].sum().sum()
print(pivot)
pivot.loc['All','All']=pivot.iloc[:-1,:-1].sum().sum()
print(pivot)
plt.bar(pivot.index[:-1],pivot['A'][:-1])
plt.xlabel('Region')
plt.ylabel('Sales of Product A')
plt.title('Sales of Product A by Region')
plt.show()



