import numpy as np
import pandas as pd

data = pd.read_csv("melbourne.csv")
# find all columns having null values
#print(data.isnull().sum())

print("---------------")

# this is equivalent to the above
#print(data.isnull().sum(axis=0))

#print(data.isnull().sum(axis=1))

#Treating missing values in columns

# find percentage of missing values in each column

#print(round(data.isnull().sum()/len(data.index)*100,2))


# removing the three columns
data = data.drop('BuildingArea', axis=1)
data = data.drop('YearBuilt', axis=1)
data = data.drop('CouncilArea', axis=1)

#round(100*(data.isnull().sum()/len(data.index)), 2)

#TReating missing values in rows
#rows having missing values greater than 5
#print(data[data.isnull().sum(axis=1) > 5])

# count the number of rows having > 5 missing values
# use len(df.index)
#print(len(data[data.isnull().sum(axis=1) > 5].index))

# retaining the rows having <= 5 NaNs
data = data[data.isnull().sum(axis=1) <= 5]

# removing NaN Price rows
data = data[~np.isnan(data['Price'])]

# removing NaNs in Landsize
#data = data[~np.isnan(data['Landsize'])]
#print(data["Landsize"].describe())

# rows having Lattitude and Longitude missing
#print(data[np.isnan(data['Lattitude'])])

#print(data.loc[:, ['Lattitude', 'Longtitude']].describe())

# imputing Lattitude and Longitude by mean values
data.loc[np.isnan(data['Lattitude']), ['Lattitude']] = data['Lattitude'].mean()
data.loc[np.isnan(data['Longtitude']), ['Longtitude']] = data['Longtitude'].mean()

#print(data.loc[:, ['Bathroom', 'Car']].describe())

# converting to type 'category'
data['Car'] = data['Car'].astype('category')

# displaying frequencies of each category
data['Car'].value_counts()

# imputing NaNs by 2.0
data.loc[pd.isnull(data['Car']), ['Car']] = 2


# converting to type 'category'
data['Bathroom'] = data['Bathroom'].astype('category')

# displaying frequencies of each category
data['Bathroom'].value_counts()


# imputing NaNs by 1
data.loc[pd.isnull(df['Bathroom']), ['Bathroom']] = 1

