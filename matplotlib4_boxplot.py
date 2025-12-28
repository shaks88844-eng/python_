import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
y=[3,6,4,7,4,9]

y1=[3,9,0,8,4,8]
y2=[y,y1]

plt.boxplot(y2)
plt.show()

#excel file
data=pd.read_excel("sales.xlsx")
print(data)
plt.boxplot(data["price"])
plt.show()