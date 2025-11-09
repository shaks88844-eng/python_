#leap year
n=int(input("enter the year: "))
if(n%400==0):
    print("Leap year")
elif((n%4==0) and (n%100!=0)):
  print("leap year")
else:
  print(" not a leap year")

