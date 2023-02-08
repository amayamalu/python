n=int(input("enter the num:"))
order=len(str(n))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit+order
    temp=temp//10
if n==sum:
    print(n,"armstrong")
else:
    print(n,"not amstrong")
