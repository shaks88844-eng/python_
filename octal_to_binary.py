#convert  octal to binary in 2 steps
num = int (input("enter a octal number that you want to convert into  binary:  "))
ans=0
multi=1
#first we convert octal into decimal
while num>0:
  rem =num%10
  num =num//10
  ans=ans+rem*multi
  multi=multi*8


num=ans
#secondly we convert decimal into binary
ans=0
multi=1
while num>0:
  rem =num%2
  num =num//2
  ans=ans+rem*multi
  multi=multi*10


print(ans)

