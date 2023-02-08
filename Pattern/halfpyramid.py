# rows=int(input("enter the no of raws:"))
# for i in range(0,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


#inverted half pyramid
rows=int(input("enter the raws:"))
for i in range(rows+1,0,-1):
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()