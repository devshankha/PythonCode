import numpy as np
# simple program to add to numpy arrays
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = array1+array2
print(array3)
# simple program to square all elements of a numpy array
list1 = np.array([2,3,4])
list1 = 2**list1
print(list1)

#3d numpy array
array_3d = np.array([[[1,2], [3,4],[5,6]]])
print(array_3d)

#common numpy
arr1 = np.zeros(5)
print(arr1)

arr1 = np.zeros(5,dtype=np.int)
print(arr1)

ass = np.ones((5,2))
print(ass)

asl = np.ones((5,2),dtype=np.int)
print(asl)

ks = np.random.random([2,2])
print(ks)

ks1 = np.random.random([3])
print(ks1)


lms = np.arange(6,20,2)
print(lms)

fgh = np.linspace(5,20,2)
print(fgh)

rand_array = numpy.array([[1,2,3], [2,3,4]])
print("Shape: {}".format(rand_array.shape))
print("dtype: {}".format(rand_array.dtype))
print("Dimensions: {}".format(rand_array.ndim))
print("Item size: {}".format(rand_array.itemsize))

a = numpy.array([[1,2,3], [2,3,4]])
print(a.shape)
print(a.shape[0])
print(a.shape[1])
print(a.ndim)
print(a.itemsize)
