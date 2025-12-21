#fuction to  find maximum  of three numbers 
def max_():
    x=89
    y=98
    z=7
    if x>y and x>z:
        print ("x is max")
    elif y>x and y>z:
        print("y is great")
    else:
        print("z is greater")

max_()
 
#write a python  function to create and print  a list where  the 
#values are  sqaure of numbers between 1   and 30
def  create_list():
    l=[]
    for i in range(1,31):
        i=i**2
        print(i)
        l.append(i)
    print(l)

create_list()

#write a function that takes a number as a parameter
#and check if the number is prime or not

def check(n):
    if n<1:
        print("not prime")
    elif n==2 :
        print("prime")    
    for i in range(2,n):
    
       if n%i==0:
            print(" not prime")
            break
    else:
            print(" prime")
            
check(71)


#write a function to sum all the numbers in a list
def sum (l):
    s=0
    for i in l:
     s=s+i
    print (s)     
     
l=[76,98,90,78,44,99]    
sum(l) 

#using recursion
def re(l):
    if len(l)==1:
        return(l[0])
    else:
       return( l[0]+re(l[1:]) ) 

print(re([8,9,8,0,7,8])  )  

#fibonacci sequence
def series(l):
    if l==1:
        return 0
    elif l==2:
       return 1
    else:
        return (series(l-1)+series(l-2))

print(series(7))
