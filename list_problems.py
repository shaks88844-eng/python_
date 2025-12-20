A=["ross","rachal","monica","joe"]

#swap first and last
A[0], A[3]=A[3], A[0]
print(A)

#add value  at second position
print(A.insert(1,"shivu"))
print(A)

#remove value at 3rd position
print(A.pop(2))
print(A)



#list 2
B=[1,13,14,12,10]

#multiple all elements
m=1
for i in B:
    m=m*i

print(m)   

#or you can use sort function
print(B.sort())
print(B[-1])

#largest number
l=B[0]
for i in B:
    if i>l:
        l=i

print(l)           



#smallest number
s=B[0]
for i in B:
    if i<s:
        s=i

print(s)   


#or you can use sort function
B.sort()
print(B[0])

   
    


