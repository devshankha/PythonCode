
'''
Given an integer 'x', create an array of size m*n having all integer values equal to 'x'.
Hint: Use dtype to specify integer.


'''
import numpy as np

a = np.empty([m, n],dtype=np.int)
a.fill(x)
print(a)
print(a.ndim)

a1 = np.array([2,3],dtype=np.int)
print(a1.ndim)



'''
Given an even integer ‘n’, create an ‘n*n’ checkerboard matrix with the values 0 and 1, using the tile function.
'''

# Read the variable from STDIN
n = int(input())

import numpy as np

# Create the smallest unit of a checkerboard matrix
x = np.array([[0, 1], [1, 0]])

# Create a checkerboard matrix of size n*n using the tile() function. We use n//2
# since the smallest unit of a checkerboard matrix is already of size 2*2. So, for
# creating a larger matrix, say, of size 8, we need to replicate it using the tile()
# function 4 times as it will then give a matrix of size 8*8.
check = np.tile(x, (n//2, n//2))

# Print the created matrix
print(check)

array_2d =np.array([[1,2,3],[4,5,6]])
print(array_2d)
#EXTRACT SECOND ROW FROM ARRAY
#print(array_2d[1,:])
#EXTRACT SECOND COLUMN FROM ARRAY
print(array_2d[:,1])
