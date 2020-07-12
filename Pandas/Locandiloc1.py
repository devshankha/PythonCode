import numpy as np
import pandas as pd

# crete a sample dataframe
data = pd.DataFrame({
    'age' :     [ 10, 22, 13, 21, 12, 11, 17],
    'section' : [ 'A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender' :  [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'favourite_color' : [ 'red', np.NAN, 'yellow', np.NAN, 'black', 'green', 'red']
})

# select all rows with a condition
#data = data.loc[data.age >= 15]
print(data)

#select rows based on multiple conditions
#data = data.loc[(data.age > 17) & (data.gender == 'm')]
#print(data)

# And if the indices are not numbers, then we cannot slice our dataframe.
#In that case, we need to use the iloc ,basically slicing using loc will only work if the indices
# are numbers
data = data.loc[0:3]
print(data)

# select few columns with a condition
#data =data.loc[(data.age >= 18), ['city', 'gender']]
#print(data)

# update a column with condition
#print(type(data.loc))
#both of the below works
data.loc[(data.age >= 12), ['section']] = 'M'
data.loc[(data.age >= 12), 'section'] = 'M'
#print(data)
print("---------------------------------------------------------")
# select rows with indexes
#data=data.iloc[[0,3]]
#print(data)

data=data.iloc[0:3]
print(data)
