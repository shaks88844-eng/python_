def aa(array,x):

    c=0
    for num in array:

     if(num==x):
      print ("your no:",num)
      print("position:",c)
     c=c+1
    
     if c==0:
       print(-1)

    


array=list([4,7,9,9,7,3,88,66])


number=int(input("enter no: "))


aa(array,number)
