
def reverse(a):
    i=0
    j=len(a)-1
    while(i<j):
        t=a[i]
        a[i]=a[j]
        a[j]=t
        i=i+1
        j=j-1
    return a



array=list([1,2,3,4,5,6,7,8])
print(reverse(array))
