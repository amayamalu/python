from Newmodule import * #all functions called-----###from Newmodule import create()

while True:
    ch=int(input("1.Create\n 2.Search\n 3.Remove\n 4.Replace \n Enter your choice:"))
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