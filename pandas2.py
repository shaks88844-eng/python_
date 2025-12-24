import pandas as p
import numpy as np
 

data=p.read_excel("Book3.xlsx")

data.loc[(data["Total"]<100)," gifts"]=" no giftss"
data.loc[(data["Total"]>100),"gifts"]="gifts"
print(data)

#add two columns
data["Total  Units"]=data["Rep"].str.capitalize()+" "+data["Item"].str.capitalize()
print(data)

#find 20% of total
data["20%"]=(data["Total"]/100)*20
print(data)

#extract first three letter from items
def extract (value):
    return  str(value)[0:3]

data["short items"]=data["Item"].map(extract)
print(data)

