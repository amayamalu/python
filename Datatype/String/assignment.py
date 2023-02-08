#1 how could you check if each word in a string begins with a capital letter

str="hello world"
print(str.istitle())

#2 check if a string contains a specific substring

a='mango'
if 'man' in a:
    print("true")
else:
    print("false")

#3 find the index of the first occurance of a substring in a string

str1="world tour"
b=str1.index('tour')
print(b)

#4 count the total no.of characters in a string

str1="python"
c=len(str1)
print(c)

#5 count the no.of specific character in a string

str2="python is a good programming language"
d=str2.count('a')
print(d)

#6 capitalize the first character of a string

str3="hello python"
print(str3.capitalize())

#7 check if a string contain only letters

str4='5648739'
print(str4.isdigit())

#8 split a string on a specific character

str5="goodmorning"
print(str5.split(' '))

#9 reverse the string "hello world"

str6="hello world"
print(str6[::-1])

#10 join a list of strings into a single string,delimited by hapens

a=['mango','orange','apple']
print(''.join(a))

#11 give an example of string slicing

string='good evening'
print(string[0:4])

#12 convert a integer to string
ab=435
print(type(ab))
abc='435'
print(type(abc))

#13 replace all instances of a substring in a string

string1="good morning"
print(string1.replace("mor","eve"))

#14 removewhite space from the left,right or both side of a string

string2="   welcome  "
print(string2.strip())

#15 replace each symbol with # in the following string

str123="/* join is @ developer & musician!!"
print(str123.replace("/","#").replace("*","#").replace("@","#").replace("&","#").replace("!","#"))

#another
# str1234="/* join is @ developer & musician!!"
# list1=['/','*','@','&','!']
# for i in list1:
#     g=str1234.replace(i,"#")
# print(g)

#16 append new string in the middle of the given string

s1="luminar"
s2="python"
p=s1[0:4]
q=s1[4:7]
r=p+s2+q
print(r)



