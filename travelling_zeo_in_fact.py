n=int(input("enter no: "))
if(n<5):
    print("0")


count=0
while(n>=5):
    count=count+n//5
    n=n//5
print(f"total zero: {count}")