import numpy as np

# creates an identity matrix
u = np.eye(2,dtype = np.int)
#print(u)


u = np.eye(3,dtype = np.int)
#print(u)

#creates transpose of a matrix
u1 = np.array([[1,2,3],[4,5,6]])

print(u1.T)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(np.linalg.inv(a))

print(np.linalg.det(a))

print(np.linalg.eig(a))

a1 = np.array([[1,2,3],[4,5,6]])
f=np.vectorize(lambda x:x**2)
print(f(a1))