def sample():
    print("Hi dears")
sample()

#add 2 number
def sum():

    a=10
    b=20
    c=a+b
    return c
print("The sum is:",sum())

#arguments&parameters
def func(name):#name is a parameter
    print("hi",name)
func("ammu")
func("manu")

#*arbitary arguments
def fun(*name):
    print("hy dears,my name is",name)
fun("ammu","anu")
fun("aju")

#keyword arguments
def funct(ch1,ch2,ch3):
    print("youngest child is " + ch1


          )
funct("ammu",ch2="anu",ch3="aju")

#arbitary keyword arguments
def my_function(**ch):
    print("last name is  " + ch["ln"])
my_function(fn="kkkkk",ln="hhhhh")



