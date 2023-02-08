str1=input("enter the string:")
str2=str1.lower()
if (str2==str2[::-1]):
    print("palindrome")
else:
    print("not palindrome")