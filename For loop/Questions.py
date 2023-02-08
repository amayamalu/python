# str1="amaya"
# for i in str1:
#     print(i)
#     print()
#
# #PROGRAM TO PRINT THE TABLE OF THE GIVEN NUMBER
# ls=[1,2,3,4,5]
# n=2
# for i in ls:
#     s=n*i
#     print(s)
#     print()
#
# #PROGRAM TO PRINT THE SUM OF GIVEN NUMBERS
# ls1=[2,4,5,6,7,1]
# s=0
# for i in ls1:
#     s=s+i
# print(s)
#
# #SUM OF N NUMBERS
# n=int(input("enter the number:"))
# s=0
# for i in range(1,n):
#     s=s+i
# print(s)
#
#
# #PRINT NUMBERS IN SEQUENCE
# for i in range(10):
#     print(i,end=" ")
#
#
# #PRINT MULTIPLICATION TABLE OF GIVEN NUMBER
# n=int(input("enter the number:"))
# for i in range(1,11):
#     c=n*i
#     print(n,"*",i,"=",c)
#
#
# #PRINT EVEN NUM USING IN STEPSIZE IN RANGE
# n=int(input("enter the num:"))
# for i in range(2,n,2):
#     print(i)
#
# """"##len()-----list##"""
# lst=["anu","ammu","anju"]
# for i in range(len(lst)):
#     print("hello",lst[i])

"""To print fibonacci series using range()"""#0 0  1 2 3 5 8 13
# n=int(input("Enter the num:"))
# sum=0
# a=0
# b=1
# for i in range(n):
#     sum=a+b
#     print(a)
#     a=b
#     b=sum
# #/
n=int(input("Enter the num:"))
a,b=0,1
print(a)
print(b)
for i in range(3,n+1):
    sum=a+b
    print(sum)
    a,b=b,sum

"""Prime number"""
n=int(input("enter the num:"))
f=0
#n=5----5%1=0,5%2==1,5%3==2,5%4==1,5%5==0
if n==1:
    print("not defined")
else:
    for i in range(1,n+1):#1----n
        if n%i==0:
            f=f+1#1,2
    if f==2:
        print("prime")
    else:
        print("not prime")

# ###
#
# #for else
# for i in "amaya":
#     print(i)
# else:
#     print("completed")

# """BREAK"""
# l=[10,20,30,40,50,100,200,250]
# for i in l:
#     print(i)
#     if (i==100):
#         break
# print()
#
# """CONTINUE"""
# l=[10,20,30,40,50,100,200,250]
# for i in l:
#     if i==100:
#         continue
#     print(i)