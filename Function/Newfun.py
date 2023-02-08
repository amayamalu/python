# def sum():
#     a,b=10,20
#     s=a+b
#     return s
# s=sum()
# print("sum is",s)
#
# """PARAMETER AND ARGUMENTS"""
# def sum(x,y):
#     s=x+y
#
#     return s
# s=sum(100,200)
# print("sum is",s)
# print(sum(20,40))
#
# """ WAP to find factorial of a num using function with return type and function parameter"""
# def fact(n):
#     fac=1
#     for i in range(1,n+1):
#         fac=fac*i
#     return fac
# fa=fact(5)
# print("factorial is",fa)
# #
#
"""DIFFERENT PARAMETERS"""
# """1.Arbitary"""
# def colour(*args):
#     print(args[0])
#     for i in args:
#         print(i)
# colour('red','blue','white')
#
# def colour(x,*args):
#     print("normal argument",x)
#     for i in args:
#         print(i)
# colour('red','blue','white')


# """2.Keyword arguments"""
# def stud(stud1,stud2,stud3):
#     print("first is:",stud1)
#     print("second is:", stud2)
#     print("third is:", stud3)
# stud(stud2="anju",stud1="anu",stud3="kiran")
# print()

#using **
def stud(**keyargs):
    for i,j in keyargs.items():
        print("%s=>%s"%(i,j))
stud(stud2="anju",stud1="anu",stud3="kiran")
print()

# """ALL ARGUMENTS IN ONE PROGRAM"""
# def student(x,*args,**kwargs):
#     print("simple argument:",x)
#     for i in args:
#         print(i)
#     for i,j in kwargs.items():
#         print("%s=>%s" % (i, j))
# student("amal","anu","arun",std2="anju",std1="amal",std3="vinu")
# print()

"""DEFAULT PARAMETER"""
def display(country='india'):
    print("I am from",country)
display()
display('america')

# """LIST"""
# def dis(ls):

#     for i in ls:
#         print(i)
# dis([10,20,30])
#
# """adding elements in to a list"""
# ls=[]
# def create():
#     n=int(input("enter the numbers limit:"))
#     for i in range(n):
#         num=int(input("enter the num:"))
#         ls.append(num)
#     print(ls)
# #create()
# #
# # """search item"""
# lst=[1,2,3,4]
# def search():
#     n=int(input("enter the num:"))
#     if n in lst:
#         print(n,"is present")
#     else:
#         print("not present")
# #search()
#
# """remove"""
# lst=[2,3,4,5,6]
# def remove():
#     n=int(input("enter the number to remove:"))
#     if n in lst:
#         lst.remove(n)
#     else:
#         print("item not found in the list")
#     print(lst)
# #remove()
#
# """replace"""
# lst=[2,3,4,5,6]
# def replace():
#     old=int(input("enter the num:"))
#     new=int(input("enter the num can be replaced:"))
#     for i in range(len(lst)):
#         if lst[i]==old:
#             lst[i]=new
#     print(lst)
# # replace()
#
# while True:
#     ch=int(input("1.Create\n 2.Search\n 3.Remove\n 4.Replace \n Enter your choice:"))
#     if ch==1:
#         create()
#     elif ch==2:
#         search()
#     elif ch==3:
#         remove()
#
#     elif ch==4:
#         replace()
#     else:
#         break
#

