import pandas as p
import numpy as np
 

data=p.read_excel("conca.xlsx")
print(data)
data2=p.read_excel("Book4.xlsx")
print(data2)

#compare
print(data.compare(data2,keep_shape=True))
print(data.compare(data2,keep_equal=True))

#pivoting(index,column,values)
print(data.pivot(index="id",columns="UnitCost",values="Total"))

#melting
print("melt")
print(data.melt(id_vars=None, value_vars=["Total","UnitCost"],value_name="total"))

print(data.melt(id_vars=None, value_vars=["UnitCost"],value_name="total"))

