import pandas as p
import numpy as np
 

data=p.read_excel("Book3.xlsx")
print(data)
data2=p.read_excel("Book4.xlsx")
print(data2)
data3=p.read_excel("conca.xlsx")
print(data3)

#merge 
print(p.merge(data,data2,on="id"))

print(p.merge(data,data2,on="id",how="left"))

#concat
print(p.concat([data2,data3]))

