import numpy as np
import pandas as pd


market_pdf  = pd.read_csv("market_fact.csv")
#looking at the top and bottom entries of a dataframe
#print(market_pdf.head)
#print(market_pdf.tail)

# Looking at the datatypes of each column
print(market_pdf.info())

# Note that each column is basically a pandas Series of length 8399
# The ID columns are 'objects', i.e. they are being read as characters
# The rest are numeric (floats or int)

# Describe gives you a summary of all the numeric columns in the dataset
#market_pdf.describe()

# Column names
#print(market_pdf.columns)

# The number of rows and columns
#print(market_pdf.shape)
#print(market_pdf.info)

# You can extract the values of a dataframe as a numpy array using df.values
arr1=market_pdf.values
print(market_pdf.head())

market_pdf.set_index('Ord_id', inplace = True)
print(market_pdf.head())

# Sorting by index
# axis = 0 indicates that you want to sort rows (use axis=1 for columns)
market_pdf.sort_index(axis = 0, ascending = False)



# Sorting by values

# Sorting in increasing order of Sales
#print(market_pdf.sort_values(by='Sales').head())

# Sorting by more than two columns

# Sorting in ascending order of Sales for each Product
#market_pdf.sort_values(by=['Prod_id', 'Sales'], ascending = False)

# Selecting alternate rows starting from index = 5
s=market_pdf[5::2]
print(type(s))

# Using df['column']
sales = market_pdf['Sales']
print(type(sales))

# IMPORTANT point here, if we give column argument as  list
# then we get a dataframe and not a series
# Using df['column']
sales1 = market_pdf[['Sales']]
print(type(sales1))



