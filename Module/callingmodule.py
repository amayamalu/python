import Newmodule

while True:
    ch=int(input("1.Create\n 2.Search\n 3.Remove\n 4.Replace \n Enter your choice:"))
    if ch==1:
        Newmodule.create()
    elif ch==2:
        Newmodule.search()
    elif ch==3:
        Newmodule.remove()
    elif ch==4:
        Newmodule.replace()
    else:
        break
