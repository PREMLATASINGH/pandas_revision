import numpy as np
import pandas as pd
data={
    'student':['raj','rani','ranu','raja'],
    'score':[70,80,87,67]
}
df=pd.DataFrame(data)
print(df)
print(df.shape)
print(df.info())
print(df.describe())
print(df.head())