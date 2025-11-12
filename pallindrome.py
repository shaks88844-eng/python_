n=int(input("enter the number: "))
ans=0
x=n
while x>0:
    r=x%10
    x=x//10
    ans=ans*10+r



if(ans==n):
    print("yes pallindrome") 
else:
    print("not a pallindrome")     
