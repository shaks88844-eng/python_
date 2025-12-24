import pandas as pd
import numpy as np
data={"name":["a","b","c"],
     "age":[33,22,45],
     "salary":[100,120,321]}
df=pd.DataFrame(data)
print(df)

#open csv file
data1=pd.read_csv("C:/Users/Acer/Desktop/New folder/Common7/IDE/Extensions/Application/SSMSIconMappings.csv")
print(data1)
print()

#open excel file
data2=pd.read_excel("Book2.xlsx", usecols=[0,1,2,3,4,5,6])
print(data2)

print(data2.head(2))
print(data2.info())
print(data2.describe())
print(data2.isnull())
print(data2.isnull().sum())

#handling duplicate values in pandas
print(data2["File no."].duplicated().sum())

#drop duplicate
print(data2.drop_duplicates("File no."))

#OPEN EXCEL 
data3=pd.read_excel("Book3.xlsx", usecols=[0,1,2,3,4,5,6])
print(data3)

#DROP NULL
print(data3.dropna())

#replace null dAta
print("replace null data")
data3["Region"]=data3["Region"].replace(np.nan,"East")
print(data3)

#replace null data from entire Data Frame
print(data3.replace(np.nan,"chup"))

#fill data (forward,backward)
print(data3.fillna(method="Ffill"))
print(data3.fillna(method="Bfill"))

