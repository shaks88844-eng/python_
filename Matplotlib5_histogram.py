
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
y=[3,6,4,7,4,9,4,9,9]

y1=[3,9,0,8,4,8]
y2=[y,y1]

plt.hist(y,bins=10)
plt.show()

#excel file
data=pd.read_excel("sales.xlsx")
print(data)
plt.hist(data["price"],bins=10,edgecolor="black", color="pink")
plt.show()