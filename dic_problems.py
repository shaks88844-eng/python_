#create dictionary
s={"a":1, "b":2, "c":9, "d":4, "e":5}


#sort dic by value
sort=sorted(s.values())
print(sort)


#print  a dic
for i,j in s.items():
    print(i,":",j)


#multiply all items in a dict

p=1
for i in s:
    p=p*s[i]
    print(p)


#create a dic keys are between 1 to 15 and the values are square  of keys
b={}
for i in range(1,16):
    b[i]=i**2   
    

print(b) 
print()

#sort  a dic by keys
dic={21:"y", 56:"o", 89:"op", 78:"09"}
t={}
t=sorted(dic)
print(t)


