ls=[]
def create():
    n=int(input("enter the numbers limit:"))
    for i in range(n):
        num=int(input("enter the num:"))
        ls.append(num)
    print(ls)
# create()
#
 # """search item"""
lst=[1,2,3,4]
def search():
    n=int(input("enter the num:"))
    if n in lst:
        print(n,"is present")
    else:
        print("not present")
# search()

"""remove"""
lst=[2,3,4,5,6]
def remove():
    n=int(input("enter the number to remove:"))
    if n in lst:
        lst.remove(n)
    else:
        print("item not found in the list")
    print(lst)
# remove()

"""replace"""
lst=[2,3,4,5,6]
def replace():
    old=int(input("enter the num:"))
    new=int(input("enter the num can be replaced:"))
    for i in range(len(lst)):
        if lst[i]==old:
            lst[i]=new
    print(lst)
# replace()