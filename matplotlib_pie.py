import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
y=[3,6,4,7,4,9]

y1=[3,9,0,8,4,8]
color=np.random.randint(1,30,6)
size=np.random.randint(10,30,6)
ex=[0,0,0,0,0,0.1]
plt.pie(y,labels=y1,shadow=True,autopct="%f",startangle=180,explode=ex)
#plt.show()

#excel file
data=pd.read_excel("Book3.xlsx")
print(data)
group=data.groupby("id")["Units"].sum()
print(group)
plt.pie(group.values,labels=group.index)
#plt.pie(data["id"],labels=data["Units"],shadow=True,autopct="%f",startangle=180)
plt.show()