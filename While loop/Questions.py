#program to print 1 to 10
i=1
while i<=10:
    print(i)
    i=i+1


#print table of given number
i=1
num=int(input("enter the number:"))
while i<=10:
    print("%d x %d=%d\n"%(num,i,num*i))
    i=i+1

#Sum of even numbers
n=int(input("enter the number"))
i=1
s=0
while i<=n:
    if(i%2==0):
        s=s+i
    i=i+1
print(s)

#AVG OG 5 NUMBERS
i=1
s=0
while i<=5:
    n=int(input("enter the %d:"%(i)))
    s=s+n
    i=i+1
avg=s/5
print(avg)


#ADDING ELEMENT TO A LIST USING WHILE LOOP
n=int(input("enter the number:"))
a=[]
i=0
while i<=n:
    a.append(i)
    i=i+1
print(a)


#PRINT SQUARE OF NUMBERS
n=int(input("enter the number:"))
s=0
i=1
while i<=n:
    s=i*i
    i=i+1
print(s)

#REVERSE A NUMBER
num=int(input("enter the number:"))
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

""" another method """
num=int(input("enter num:"))
i=0
str1=str(num)
while i<len(str1):
    i=i+1
print(str1[::-1])



#PRINT EVEN &ODD B/W 1 TO 100
n=int(input("enter the number:"))
i=1
while i<=n:
    print(i,end=" ")
    if i%2==0:
        print("even")
    else:
        print("odd")
    i=i+1