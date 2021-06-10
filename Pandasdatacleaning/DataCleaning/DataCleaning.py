import os
import numpy as np
import pandas as pd
print(os.getcwd())
inp0 = pd.read_csv("googleplaystore_v2.csv")
#inp0.drop(['App','Category','Rating'],axis=1,inplace=True)

inp0.shape
# Remove rows having null Rating
inp0 = inp0[~inp0.Rating.isnull()]

#cross check, Rating column should have  zero null values
inp0.Rating.isnull().sum()
inp0.isnull().sum()

#understand nulls for the column android version
#printing rows having android version as null
#inp0[inp0['Android Ver'].isnull()]

# remove that single row having android version as null and cateory as 1.9 
inp0=inp0[~(inp0['Android Ver'].isnull() & (inp0.Category == "1.9"))]

inp0[inp0['Android Ver'].isnull()]


inp0['Android Ver'].value_counts()


inp0['Android Ver'].mode()

#inp0['Android Ver'].mode()[0]

#Imputation, replace missing values in android column with the mode
inp0['Android Ver'] =inp0['Android Ver'].fillna(inp0['Android Ver'].mode()[0])

# this will help you check the datatypes of the different columns
inp0.dtypes

#check  values in the price column
inp0.Price.value_counts()

#remove the dollar symbol in price so that it becomes int or float
#this does-not seem to be working
inp0.Price =inp0.Price.apply(lambda x: 0 if x==0  else  float(x[1:]))

#Write the function to make the changes
#this also doesnt seem to work
#basically reviews is object change it into int
inp0.Reviews = inp0.Reviews.astype("int32")
