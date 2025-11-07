num = int(input("enter octal number that you want to convert into decimal:  "))
ans=0
multi=1
while num>0:
  rem =num%10
  num =num//10
  ans=ans+rem*multi
  multi=multi*8


print(ans)
