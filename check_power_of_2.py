#power of 2
#reverse  integer
n=int(input("enter the number: "))
if n<=0:
 print("false")

if n==1:
 print("true")
else: 
  while n%2==0:
     n=n//2

if n==1:
 print("true")
else:
  print("false")
