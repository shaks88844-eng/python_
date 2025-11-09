#reverse  integer
n=int(input("enter the number: "))
multi=1
ans=0
while n>0:
   rem=n%10
   n=n//10
   ans=ans*10+rem
   multi=multi*10
print(ans)