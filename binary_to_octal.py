#convert binary to octal in 2 steps
num = int (input("enter a  binary number that you want to convert into octal:  "))
ans=0
multi=1
#first we convert binary into decimal
while num>0:
  rem =num%10
  num =num//10
  ans=ans+rem*multi
  multi=multi*2


num=ans
#secondly we convet decimal into octal
ans=0
multi=1
while num>0:
  rem =num%8
  num =num//8
  ans=ans+rem*multi
  multi=multi*10


print(ans)

