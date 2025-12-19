num=input("enter a string")


#reverse string
b=(num[::-1])
print(b)

#check  a string contains only digit
print(num.isdigit())

#if a sting is palindrome
if b==num:
    print("yes pallidrome")
else:
    print("no it is not pallindrome")

#find no of vowels in String
vowel=0
for i in num:
  if  i=="a"or i=="e"or i=="i"or i=="o"or i=="u": 
    vowel=vowel+1

print(vowel)
    
#check if every word in string begins with capital letter
print(num.istitle() )
