# # """HALF PYRAMID"""
# # n=int(input("enter the raws:"))
# # for i in range(1,n+1):
# #     for j in range(i):
# #         print("*",end=" ")
# #     print
# #
# # n=int(input("enter the raws:"))
# # for i in range(n+1,1,-1):
# #     for j in range(i-1,0,-1):
# #         print("*",end=" ")
# #     print()
# #
#
# """FULL PYRAMID---one increment"""
# # n=int(input("enter the raws:"))
# # for i in range(n):
# #     for s in range(n-i-1):
# #         print(" ",end=" ")
# #     for j in range(i+1):
# #         print(" * ",end=" ")
# #     print()
#
#
# """3 increment"""
# # n=int(input("enter the raws:"))
# # for i in range(n):
# #     for s in range(n-i-1):
# #         print("  ",end=" ")
# #     for j in range(2*i+1):
# #         print("* ",end=" ")
# #     print()
#
# # """inverted"""
# # n=int(input("enter the raws:"))
# # for i in range(n):
# #     for s in range(i):
# #         print(" ",end=" ")
# #     for j in range(n-i):
# #         print(" * ",end=" ")
# #     print()
#
#
# """hollow"""
# # n=int(input("enter the raws:"))
# # for i in range(n):
# #     for j in range(n):
# #         if i==0 or j==0 or i==n-1 or j==n-1:
# #             print("*",end="  ")
# #         else:
# #             print("  ",end=" ")
# #     print()
#
#
# """ALPHABETIC ---V"""
# a=0
# b=6
# for i in range(4):
#     for j in range(7):
#         if i==j:
#             print("*",end=" ")
#         elif i==a and j==b:
#             a=a+1
#             b=b-1
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
#
# """ALPHABETIC -----X"""
# a=0
# b=4
# for i in range(5):
#     for j in range(5):
#         if  i==a and j==b:
#             print("*", end=" ")
#             a=a+1
#             b=b-1
#         elif i==j:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()

"""HOLLOW DIAMOND"""
for i in range(7):
    for j in range(7):
        if i+j==3 or j-i==3 and  i-j==3 or j+i==9:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
