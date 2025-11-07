num = int(input("enter binary number:  "))
ans=0
multi=1
while num>0:
  rem =num%10
  num =num//10
  ans=ans+rem*multi
  multi=multi*2


print(ans)
