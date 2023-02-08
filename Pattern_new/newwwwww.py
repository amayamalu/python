# n=int(input("enter the num:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# #
# n=int(input("enter the num:"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()
#


# n=int(input("enter the num:"))
# for i in range(n):
#     for s in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(" * ",end=" ")
#     print()
#
# # n=4
# for i in range(n-1):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):

#         print(" * ",end=" ")
#     print()
#
#
# """A"""
# n=int(input("raw:"))
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or (i==0 or i==3) and (j>0 and j<4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#
# """hollow diamond"""
# for i in range(5):
#     for j in range(5):
#         if i+j==2 or j-i==2 or i-j==2 or i+j==6:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
#












