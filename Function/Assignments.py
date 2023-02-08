"""1. To create and print a list where values are square of numbers b/w 1 and 30(both included)"""

def list_creation():
    l=list()
    for i in range(1,31):
        l.append(i**2)
    print(l)
list_creation()



"""3.Assign a different name to  function and call it through the new name"""

def sum(a,b):
    c=a+b
    return c
s=sum
print(s(2,4))


""" 4. Generate a pyton list of all the even numbers b/w 4 to 30"""
def even():
    l=[]
    for i in range(4,31):
        if i%2==0:
            l.append(i)
    print(l)
even()


""" 5.Function returns a tuple"""

def person():
    return "ammu",20,"software"
print(person())



"""6.Define a function which counts vowels and consonent"""

word=input("enter the word")
def count(val):
    vowels=0
    consonent=0
    v=["a","i","e","o","u"]
    for i in word:
        if i in v:
            vowels=vowels+1
        else:
            consonent=consonent+1
    print("the count of vowels is:",vowels)
    print("the count of consonent is:", consonent)
count(word)

"""7.present or absent"""

def stdnts(n):
    l=[1,2,3,4,5,6]
    if n in l:
        print("present")
    else:
        print("absent")
stdnts(4)



"""8.Return the maximum od 3 numbers"""

def max(a,b,c):
    if a>b and a>c:
        print("a is max")
    elif b>c and b>a:
        print("b is max")
    elif c>a and c>b:
        print("c is max")
max(3,6,1)

"""" 2 numbers of arguments and return the sum"""
def add(a,b):
    print("the sum is",a+b)
add(2,3)

"""function that accepts different values as parameters and returns a list"""
def myfunc(*n):
    l=[]
    for i in n:
        l.append(i)
    print(l)
myfunc("anu","aju","ammu")

""" function that accepts 2 values and return its sum ,subtraction,multiplication"""
def operations(a,b):
    print("the sum is",a+b)
    print("the subtraction is ",a-b)
    print("the multiply is ",a*b)
operations(4,5)

"""access inner function in a function"""
def test(a):
    def add(b):
        nonlocal a
        a+=1
        return a+b
    return add(8)
func=test(4)
print(func)
