str1=input("enter the 1 st string")
str2=input("enter the  2 nd string")
str1=str1.lower()
str2=str2.lower()
if (len(str1)==len(str2)):
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)
    if (sorted_str1==sorted_str2):
        print(str1 + " and " + str2  +"are anagram")
    else:
        print(str1 + " and " + str2 +" are not anagram")
else:
    print("invalid")


