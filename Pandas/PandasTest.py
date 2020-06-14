import numpy as np
import pandas as pd

data = [0,1,2]
df = pd.DataFrame(data)
print(df)

print()

data = [0,1,2,3]
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame({"Name":["Anand","Hussain","David"],"Age":[22,34,45]})
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)


#Series can also be added as numpy arrays
arr1 = pd.Series([1,2,3])

#Pandas 


arr2 = pd.Series([4,5,6])

arr3 = arr1+arr2
print(arr3)


print(arr1[:3])

print(arr1[-4:])


#apply method of series
ar =arr1.apply(lambda x:x**2)
print(ar)

list = ["how","are","you"]
s1 = pd.DataFrame(list)
print(s1)
s1.columns="fff"

print(s1.columns)

keys become colum names
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

df = pd.DataFrame(dict)
print(df)

# Indexing explicitly
pd.Series([0, 1, 2], index = ['a', 'b', 'c'])

# You can also give the index as a sequence or use functions to specify the index
# But always make sure that the number of elements in the index list is equal to the number of elements specified in the series

pd.Series(np.array(range(0,10))**2, index = range(0,10))
