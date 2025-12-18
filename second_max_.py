def  max1(a):
    x=a[0]
    y=a[0]
    for num in a:
        if num>x:
            y=x
            x=num

    
    print("largest number is:",x)
    
    print("2nd largest number is:",y)

        
         
                 
array=list([1,2,3,6,4,55,66,43,22])

max1(array)