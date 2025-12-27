import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
y=[3,6,4,7,4,9]

y1=[3,9,0,8,4,8]
color=np.random.randint(1,30,6)
size=np.random.randint(10,30,6)
#plt.scatter(y,y1,c=color,s=size)
#plt.colorbar()
#plt.show()

#excel file
data=pd.read_excel("Book3.xlsx")
print(data)
plt.scatter(data["id"],data["Units"])
plt.show()