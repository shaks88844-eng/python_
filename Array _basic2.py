import numpy as np
a=np.array([[4,8,45,48,34],[46,4,6,77,7]])
b=np.array([[34,54,65,11,2],[56,4,5,7,8]])
print(a)
c=np.array([2])
#basic mathematical function
print("add:")
print(np.add(a,b))
print("multipy:")
print(np.multiply(a,b))
print("pow:")
power1=(np.pow(a,c))
print(power1)
print("sqrt:")
print(np.sqrt(power1))

print("exp:")
print(np.exp(a))