import numpy as np
import pandas as pd

# List of Tuples
empoyees = [('jack', 34, 'Sydney', 5,"Ecity",7714) ,
         ('Riti', 31, 'Delhi' , 7,"Gur",55624) ,
         ('Aadi', 16, np.NaN, 11,"Bomma",345) ,
         (np.NaN, np.NaN,'Delhi' , np.NaN,"Kalyani",7789) ,
         ('Veena', 33, 'Delhi' , 4,"Kafi",334) ,
         ('Shaunak', 35, 'Mumbai', 5,"Riaz" ,7781),
         ('Sam', 35, 'Colombo', 11,"Hamir",781),
         (np.NaN, np.NaN, np.NaN, np.NaN)
          ]
# Create a DataFrame object
df = pd.DataFrame(empoyees, columns=['Name', 'Age', 'City', 'Experience','Address','phone'])
print(df)
print("-------------")
#drop all rows with null values
df = df.dropna()

#drop  rows with more than 2  null values
df = df.dropna(thresh=2)

print(df)
#drop rows having null for city, pure pandas way
df = df[pd.notnull(df["City"])]
print(df)
