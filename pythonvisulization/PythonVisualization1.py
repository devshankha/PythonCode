import os
import numpy as np
import pandas as pd
print(os.getcwd())

#read the dataset and check the first five rows

inp0 = pd.read_csv("googleplaystore_v2.csv")
print(inp0.head())

#Check the shape of the dataframe

inp0.shape

#Check the datatypes of all the columns of the dataframe
inp0.info()

#Check the number of null values in the columns

inp0.isnull().sum()

#Drop the rows having null values in the Rating field


inp1 = inp0[~inp0.Rating.isnull()]


#Check the shape of the dataframe
inp1.shape

# Check the number of nulls in the Rating field again to cross-verify
#inp1.Rating.isnull().sum()
inp1.Rating.isnull().sum()

#Inspect the nulls in the Android Version column
inp1[inp1['Android Ver'].isnull()]

#Drop the row having shifted values

#inp1[(inp1['Android Ver'].isnull() & (inp1.Category == "1.9"))]

inp1 = inp1[~(inp1['Android Ver'].isnull() & (inp1.Category == "1.9"))]

#Check the most common value in the Android version column
inp1['Android Ver'].value_counts()

inp1['Android Ver'].mode()[0]

#this will give value as string 
inp1['Android Ver'].mode()[0]

#Fill up the nulls in the Android Version column with the most common value above value
inp1['Android Ver']=inp1['Android Ver'].fillna(inp1['Android Ver'].mode()[0])
