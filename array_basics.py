import numpy as np

a= np.array([56,45,67,34])
print(a)
print(type(a))


#slicing
print(a[1:4])
print(a[2:])
print(a[:2])


a1=np.array([[56,45,34],[45,45,33]])
print(a1)
print()
print()
#slicing
print(a1[0:2,0:2])
print()
print(a1[2:,2:])
print()
print(a1[:2,:2])

#shape function
print(np.shape(a1))

print(np.ndim(a1))
print(a1.dtype)
