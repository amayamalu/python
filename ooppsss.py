# class A:
#     def display(self,a,b):
#         print("sum is:",a+b)
# obj=A()
# obj.display(10,20)
# """single inheritance"""
# class A():
#     def display(self,a,b):
#         self.a=a
#         self.b=b
# class B(A):
#     def sum(self):
#         print("sum is:",self.a+self.b)
# obj=B()
# obj.display(10,20)
# obj.sum()
#
# """multilevel inheritance"""
# class A():
#     def display(self):
#         self.x=int(input("enter the num:"))
#         self.y=int(input("enter the num:"))
# class B(A):
#     def sum(self):
#         self.s=self.x+self.y
#         print("sum is :",self.s)
# class C(B):
#     def avg(self):
#         print("avg is:",self.s/2)
# obj=C()
# obj.display()
# obj.sum()
# obj.avg()

# """multiple inheritance"""
#
# class A():
#     def display(self):
#         self.name=input("name:")
#         self.age=int(input("age:"))
# class B():
#     def details(self):
#         self.salary=int(input("enter the salary"))
# class C(A,B):
#     def emp(self):
#         print(self.name)
#         print(self.age)
#         print(self.salary)
# obj=C()
# obj.display()
# obj.details()
# obj.emp()

# """hierarchical inheritance"""
# class A():
#     def display(self):
#         self.x=int(input("num:"))
#         self.y=int(input("num:"))
#
# class B(A):
#     def sum(self):
#         print("sum is :",self.x+self.y)
# class C(A):
#     def avg(self):
#         print("avg is:",(self.x+self.y)/2)
# class D(A):
#     def product(self):
#         print("product is:",self.x*self.y)
# obj=B()
# obj.display()
# obj.sum()
# obj1=C()
# obj1.display()
# obj1.avg()
# obj2=D()
# obj2.display()
# obj2.product()
#
#
# """constructor"""
# class A:
#     def __init__(self):
#         print("non-parameterized")
# obj=A()
#
# #
# class B:
#     def __init__(self,name):
#         print("parameterized")
#         self.name=name
#     def display(self):
#         print("my name is:",self.name)
# obj=B("anu")
# obj.display()


# """destructor"""
# class A:
#     def __init__(self,name):
#         print("parameterized")
#         self.na=name
#     def __del__(self):
#         print("destructor")
#     def display(self):
#         print("name is:",self.na)
# obj=A("malu")
# del obj
# obj.display()

"""super function"""
class parent:
    def __init__(self,txt):
        self.message=txt
    def printmessage(self):
        print(self.message)
class child(parent):
    def __init__(self,txt):
        super().__init__(txt)
obj=child("hello")
obj.printmessage()

















