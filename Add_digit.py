#Add digit
ans=0
n= int(input("enter the number: "))
while n>9:

    while n>0:
     rem=n%10
     n=n//10
     ans=ans+rem

n=ans


print(ans)