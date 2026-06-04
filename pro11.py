import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data={'employee_id':[1,2,3,4,5,6,7,8,9,10],
    'years_experience':[1,2,3,4,5,6,7,8,9,10],
    'salary':[30000,35000,40000,45000,50000,55000,60000,65000,70000,75000],
    'department':['HR','Finance','IT','Marketing','HR','Finance','IT','Marketing','HR','Finance']
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.describe())
print(df.info())
df.loc[5,'salary']=np.nan
print(df)
print(df.dropna())