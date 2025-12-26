import matplotlib.pyplot as plt
import pandas as pd
y=[3,6,4,7,4,9]
x=["a","b","c","d","e","f"]
y1=[3,9,0,8,4,8]
#plt.plot(x,y,marker="*", ls="--", label="week1")
#plt.plot(x,y1,marker="*", ls=":", color="green",label="week2",alpha=0.5)




#plot chart from excel data
data=pd.read_excel("Book3.xlsx")
print(data)
group=data.groupby("Item")["Units"].sum()
print(group)
plt.plot(group.index,group.values)


plt.legend()
plt.show()