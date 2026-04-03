import numpy as np
import pandas as pd
data={
    'employee_id':[1,2,3,4,5],
    'name':['Alice','Bob','Charlie','David','Eve'],
    'department':['HR','IT','Finance','IT','HR'],
    'salary':[50000,60000,55000,70000,52000],
    'join_date':['2020-01-15','2019-03-10','2021-06-20','2018-11-05','2020-09-30']
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())