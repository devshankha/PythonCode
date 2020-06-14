import numpy as np
import pandas as pd


market_pdf  = pd.read_csv("market_fact.csv")
#print(market_pdf.head())

#print(market_pdf.iloc[2,3])

# Selecting a single element
# Note that 2, 4 corresponds to the third row and fifth column (Sales)
#print(market_pdf.iloc[2, 4])


# Selecting a single row, and all columns
# Select the 6th row, with label (and index) = 5
print(market_pdf.iloc[5])

print("___________________")


# The above is equivalent to this
# The ":" indicates "all rows/columns"
print(market_pdf.iloc[5, :])

print("___________________")

# equivalent to market_pdf.iloc[5, ]

print(market_pdf.iloc[5, ])

print("___________________")
#print(market_pdf.iloc[2])

print("-----------")

# Select multiple rows using a list of indices
market_pdf.iloc[[3, 7, 8]]
# Equivalently, you can use:
market_pdf.iloc[[3, 7, 8], :]

# Selecting rows using a range of integer indices
# Notice that 4 is included, 8 is not
market_pdf.iloc[4:8]

# or equivalently
market_pdf.iloc[4:8, :]

# or market_pdf.iloc[4:8, ]

# Selecting a single column
# Notice that the column index starts at 0, and 2 represents the third column (Cust_id)
market_pdf.iloc[:, 2]

# Selecting multiple columns
market_pdf.iloc[:, 3:8]

# Selecting multiple rows and columns
market_pdf.iloc[3:6, 2:5]
