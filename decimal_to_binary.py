num = int(input("Enter a number: "))
print(num)
multi=1
ans=0

while num>0:
    rem =num%2
    num =num//2
    ans=ans+rem*multi
    multi=multi*10


print(ans)

