rows=int(input("enter the raws"))
for i in range(0,rows):
    for s in range(rows-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()

#inverted

r=int(input("enter the raw:"))
for i in range(r,0,-1):
    for s in range(r-i-1):
        print(" ",end="")
    for j in range(i-1,0,-1):
        print("* ",end="")
    print()
