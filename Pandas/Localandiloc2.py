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



# And if the indices are not numbers, then we cannot slice our dataframe.
#In that case, we need to use the iloc ,basically slicing using loc will only work if the indices
# are numbers
#d = data.loc[0:3]
#print(d)


#d = data.iloc[0:3]
#print(d)



# gives element in the 0th row and 3rd column
d = data.iloc[0,3]
print(d)

print("--------------------------")

#this gives 0th row and 3rd row
d = data.iloc[[0,3]]
#print(d)

# select rows with particular indexes and particular columns
d = data.iloc[[0,2],[1,3]]
print(d)

# select a range of rows and columns
d =data.iloc[1:3,2:4]
print(d)



