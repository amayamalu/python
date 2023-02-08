# """1.Write a program to print characters from a string that are present at an even index number"""
#
# str1=input("Enter the string:")
# print("The string is",str1)
# l=len(str1)
# print("Characters at even index number are:")
# for i in range(0,l,2):
#     print(str1[i])
#
# """2.Pyramid of horizontal number tables"""
#
# rows=int(input("enter the num:"))
# for i in range(1,rows+1):#1,2,3,4,5,6,7
#     for j in range(1,i+1):
#         print(i * j,end=" ")
#
#     print()
#
# """3.check if two lists have common elements"""
# l1=[2,8,5,3,9]
# l2=[2,8,1,10,44]
# l3=[]
# for i in range(len(l1)):
#     for j in range(len(l2)):
#         if l1[i]==l2[j]:
#             l3.append(l1[i])
# if len(l3)==0:
#     print(" nocommon elements")
# else:
#     print("common elements",l3)
#
#
# """4..Program to print all numbers in a range divisible by a number"""
# lower=int(input("enter the lower limit:"))
# upper=int(input("enter the upper limit:"))
# n=int(input("enter the num:"))
# for i in range(lower,upper+1):
#     if i%n==0:
#         print(i)


"""threading"""
import threading
def coder(number):
    print("coders:",number)
    return
threads=[]
for i in range(5):
    t=threading.Thread(target=coder,args=(i,))
    threads.append(t)
    t.start()
