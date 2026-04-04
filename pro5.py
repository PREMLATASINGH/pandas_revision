import numpy as np 
import pandas as pd
Data={'emp_name':["A","B","C","D","E","F","G","H","I","J"],
      "department":['HR','IT','Finance','HR','IT','Finance','HR','IT','Finance','HR'],
      "salary":[50000,60000,55000,52000,62000,58000,51000,61000,57000,53000],
      "experience":[2,5,3,4,6,1,3,7,2,4]

}
df=pd.DataFrame(Data)
print(df)
print(df.head())
print(df.tail())