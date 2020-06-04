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