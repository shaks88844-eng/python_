a=int(input("enter  the recent position of column:"))
b=int(input("enter the recent position of  rows "))
def check(a,b):
  if(a>0):
    count=0
  count=count+min(8-a,8-b)
  count=count+min(8-a,b-1)
  count=count+min(a-1,b-1)
  count=count+min(a-1,8-b)
  return count

d=check(a,b)
print(d)