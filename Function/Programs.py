# #calculator
# def add(n1,n2):
#     print("Result is :",n1+n2)
# def substraction(n1,n2):
#     print("Result is :",n1-n2)
# def multiplication(n1,n2):
#     print("Result is :",n1*n2)
# def division(n1,n2):
#     print("Result is :",n1/n2)
# n1=int(input("Enter the frst no:"))
# n2=int(input("Enter the second no:"))
# choice=int(input("enter the choice:1 2 3 4 \n"))
# if choice==1:
#     add(n1,n2)
# elif choice==2:
#     substraction(n1,n2)
# elif choice==3:
#     multiplication(n1,n2)
# elif choice==4:
#     division(n1,n2)
# else:
#     print("invalid")

# #MULTIPLY ALL THE NUMBERS IN A LIST USING FUNCTION
# list1=[1,2,3,4,5]
# def func(list1):
#     m=1
#     for i in list1:
#         m=m*i
#     print("result is :",m)
# func(list1)
#
# #WRITE A PROGRAM TO REVERSE A STRING
# str1=input("enter a string")
# def rev(str1):
#     words=str1[::-1]
#     print(words)
# rev(str1)
#
# #TO CALCULATE THE FACTORIAL OF A NUMBER(A NON NEGATIVE).THE FUNCTION ACCEPTS THE NUMBER AS AN ARGUMENT
# num=int(input("enter the num:"))
# def fact(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)
# fact(num)
#
# #PY FUNCTION THAT TAKES A NUMBER AS A PARAMETER AND CHECK THE NUMBER IS PRIME OR NOT
num=int(input("enter the num:"))
def func(num):
    if num>1:
        for i in range(0,10):
            if num%i==0:
                print(num,"it is not prime")
                break
            else:
                print(num,"it is prime")
func(10)

#CREATE AN INNER FUNCTIN TO CALCULATE THE ADDITION IN THE FOLLOWING WAY
# n1=int(input("enter frst no:"))
# n2=int(input("enter scnd no:"))
# def add(n1,n2):
#     def sum(n1,n2):
#         return n1+n2
#     print(sum(n1,n2)+5)
# add(n1,n2)
#
# #GENERATE A PYTHON LIST OF ALL THE EVEN NUMBERS BW 4 TO 30
# def even():
#     list1=[]
#     for i in range(4,30,2):
#         list1.append(i)
#     print(list1)
# even()







