import pandas as p
import numpy as np
 

data=p.read_excel("Book3.xlsx")
print(data)
gp=data.groupby(["Region"]).agg({"Total":"min"})
print(gp)