import numpy as np
import pandas as pd

# List of Tuples
empoyees = [('jack', 34, 'Sydney', 5) ,
         ('Riti', 31, 'Delhi' , 7) ,
         ('Aadi', 16, np.NaN, 11) ,
         (np.NaN, np.NaN,'Delhi' , np.NaN) ,
         ('Veena', 33, 'Delhi' , 4) ,
         ('Shaunak', 35, 'Mumbai', 5 ),
         ('Sam', 35, 'Colombo', 11),
         (np.NaN, np.NaN, np.NaN, np.NaN)
          ]
# Create a DataFrame object
data = pd.DataFrame(empoyees, columns=['Name', 'Age', 'City', 'Experience'])

print(data)

# returns true for null values
print(data.isnull())

# Will tell you the nulls in each column,that is, summing nulls columnwise
# summing up the missing values (column-wise)
print(data.isnull().sum())

#missing value in each row
print(data.isnull().sum(axis=1))


# columns having atleast one missing value
print(data.isnull().any())

#This is equivalent, by default any operates on columns
# above is equivalent to axis=0 (by default, any() operates on columns)
print(data.isnull().any(axis=0))


# rows having atleast one missing value
print(data.isnull().any(axis=1))




# rows having at least one missing value
data.isnull().any(axis=1)

# rows having all missing values
data.isnull().all(axis=1)

