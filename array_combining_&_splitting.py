import numpy as np
a=np.array([[34,3,5,6,7],[7,8,9,10,11]])
b=np.array([[4,6,7,7,8,],[34,56,1,2,8]])

#concatenate
#vertically
print(np.concatenate([a,b],axis=0))
print(np.vstack([a,b]))

#horizontally
print(np.hstack([a,b]))
print(np.concatenate([a,b],axis=1))

#splitting arrays
print()

c=np.array([34,3,5,6,7,8])
d=(np.array_split(c,2))
print(d[0])



