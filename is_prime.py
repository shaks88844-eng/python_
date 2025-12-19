num=int(input("enter a number:"))
if num<=1:
    print("no it is not prime")


for i in range(2,num):
        if num%i==0:
            print("it is not prime")
            break
        else:   
            print("yes prime")
            break