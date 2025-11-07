num = int(input("enter a number that you want to convert into octal:  "))
ans=0
multi=1
while num>0:
  rem =num%8
  num =num//8
  ans=ans+rem*multi
  multi=multi*10


print(ans)
