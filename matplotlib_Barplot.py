import matplotlib.pyplot as plt
import pandas as p
y=[3,6,4,7,4,9]
x=["a","b","c","d","e","f"]
print("create barchart from dataframe")
#plt.bar(x,y,color="pink",)
#plt.xlabel("name",fontsize=12)
#plt.ylabel("numbers")
#plt.title("dekho na")
#plt.show() 


#creater bar chart from excel file
data=p.read_excel("Book3.xlsx")
print(data)
grouped=data.groupby("Item")["Units"].sum()
print(grouped)
plt.bar(grouped.index,grouped.values)

plt.show()
