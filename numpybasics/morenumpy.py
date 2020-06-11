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
