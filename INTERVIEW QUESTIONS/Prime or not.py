"""list"""
ls=[ ]
def create():
    num=int(input("enter the limit num:"))
    for i in range(num):
        n=int(input("enter the numbers:"))
        ls.append(n)
    print(ls)
# create()

def search():
    num=int(input("num to be search:"))
    if num in ls:
        print("find")
    else:
        print("not found")
# search()

def remove():
    num=int(input("enter the num to be remove:"))
    if num in ls:
        ls.remove(num)
        print(ls)
# remove()

def replace():
    old=int(input("num to be replaced:"))
    new=int(input("enter the num:"))
    for i in len(ls):
        if ls[i]==old:
            ls[i]=new
    print(ls)
# replace()


while True:
    ch=int(input("1.create \n 2.search \n 3.remove \n 4.replace \n your choice:"))
    if ch==1:
        create()
    elif ch==2:
        search()
    elif ch==3:
        remove()
    elif ch==4:
        replace()
    else:
        break








