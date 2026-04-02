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