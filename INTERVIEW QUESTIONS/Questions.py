# """ To find all numbers such which are divisible by 7 but are not multiple of 5,b/w 2000 and 3200.printed in comma seperated sequence
# """
# # l=[]
# # for i in range(2000,3200):
# #     if (i%7==0) and (i%5!=0):
# #         l.append(str(i))
# # print(",".join(l))
#
# """1..write a Python function to find the Max of three numbers"""
# #
# def max_three(x,y,z):
#     if x>y and x>z:
#         return x
#     elif y>x and y>z:
#         return y
#     else:
#         return z
# print(max_three(56,3,78))
#
#
# """2..Write a Python function to sum all the numbers in a list"""
#
# def sum(numbers):
#     total = 0
#     for i in numbers:
#         total =total+i
#     return total
# print(sum((8, 2, 3, 0, 7)))
#
# """3.. Write a Python function to multiply all the numbers in a list."""
#
def multi(num):
    m=1
    for i in num:
        m=m*i
    return m
print(multi((5,4,9,6)))

#
# """4..Write a Python program to reverse a string."""
#
def reverse(name):
   # str="anju"
    x=name[::-1]
    print(x)
print(reverse("anju"))

""" OR """
#


#
# """5..Write a Python function to check whether a number falls in a given range"""
#
# # def test_range(n):
# #     if n in range(3,9):
# #         print( " %s is in the range"%str(n))
# #     else :
# #         print("The number is outside the given range.")
# # test_range(5)
#

# """6..Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters"""
# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])
#
# string_test('The quick Brown Fox')

# def num(n):
#     s=0
#     for i in range(0,n):
#
#         s=s+i
#         return s
# n=int(input("enter the number"))
# print(num(n))

#
# def sum(num):
#     if num==1:
#         return 1
#     else:
#         a=num+sum(num-1)
#         return a
# print(sum(10))


###############################
# def cal(a,b):
#     def add(a,b):
#         res=a+b
#         return res
#     def sub(a,b):
#         resu=a-b
#         return resu
# print(cal(10,5))

def fact(num): #sum()
    if num==1:
        return 1
    else:
        a=num*fact(num-1) #a=num+sum(num-1)
        return a

print(fact(5))


def calcu(a,b):
    sub=a-b
    add=a+b
    mul=a*b
    div=a/b
    return sub,add,mul,div
print(calcu(6,8))


# sqare of a number

def sqare():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    #print(l)
    return l

print(sqare())




def s(v):
    sq=v*v
    return sq
print(s(35))



