import numpy as np
arra1 = np.array([[2,3,1],[4,5,7]])
print(arra1)
print("Dimension is {}".format(arra1.shape))
print("Dtype is {}".format(arra1.dtype))
print("ndim is {}".format(arra1.ndim))
print("itemsize is {}".format(arra1.size))
print("itemsize is {}".format(arra1.itemsize))
print(arra1[0,])

arra4 = np.array((4,5))
print(arra4.shape)
print(arra4.ndim)


arra2 = np.array([[2,3,1]])
print("Dimension is {}".format(arra2.shape))
print("Dtype is {}".format(arra2.dtype))
print("ndim is {}".format(arra2.ndim))
print("itemsize is {}".format(arra2.itemsize))
print("itemsize is {}".format(arra2.size))

arra3 = np.arange(24).reshape(2,3,4)
print(arra3)


# functions to calculate sum, max etc from an array
arra1 = np.array([5,6,3,2,1,9])
print(np.max(arra1))
print(np.min(arra1))
print(np.sum(arra1))
print(np.average(arra1))

# functions to create an array and fill it with a number
#not you must use empty, also fill should be called in next line
#els eit fails

fl = np.empty([5],dtype = np.int)
fl.fill(7)
print(fl)

f2 = np.empty([2,3],dtype=np.int)
f2.fill(8)
print(f2)


# functions through an array
B = np.array([4,16,64],dtype = np.int)
print(B)
print(np.exp(B))

print(np.sqrt(B))

print(np.sin(B))

C = np.array([2])
print(np.exp(C))

# vstack and hsatck functions
# point to remember == call vstack with (()) and not ()

a1 = np.array([1,2,3])

a2 = np.array([4,5,6])

print(np.vstack((a1,a2)))


print(np.hstack((a1,a2)))
