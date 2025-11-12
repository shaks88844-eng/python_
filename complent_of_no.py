x=int(input("enter the number: "))
ans=0

m=1
while x>0:
  r=x%2
  r=r^1
  x=x//2
  ans=ans+m*r
  m=m*2

print(ans)
  
  

 






