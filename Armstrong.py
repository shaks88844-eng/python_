n=(input("enter no: "))
#count the digit
no=int(n)
def digit(n):
    
    count=len(n)
    return count
      
p=digit(n)
#print(p)
#print(no)

#calculate the power
def arms(no,p):
    temp=no
    ans=0
    while(temp>0):
     r=temp%10
    
     ans=ans+(r**p)
     
     temp=temp//10

    
    return ans


final_ans=arms(no,p) 
#print(final_ans)   

#check if a no is armstrong or not
if(final_ans==no):
   print("yes armstrong")
else:
   print("no ")