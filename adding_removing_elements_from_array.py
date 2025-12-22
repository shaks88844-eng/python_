import numpy as np
a=np.array([[3,4,5,6,7,0],[6,9,8,9,6,9]])

#append elements in array
print(np.append(a,3))

#insert elements in array
print(np.insert(a,0,[0,0],axis=1))

#delete elements in array
print(np.delete(a,0,axis=1))


