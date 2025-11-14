a=int(input("enter height1 "))
b=int(input("enter height2  "))
c=int(input("enter breath1  "))
d=int(input("enter breath2  "))
if((a==b and c==d)or(a==c and b==d)or(a==d and c==b)):
 print("yes  it is rectangle")
else:
  print("no it is rectangle")