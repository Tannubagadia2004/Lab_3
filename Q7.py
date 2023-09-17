# calculate sum and multiplication of complex no.
a=int(input("enter first real no. :"))
b=int(input("enter first imaginary no. :"))
if b<0:
    print(a,b,"i")
else:
    print(a,"+",b,"i")

c=int(input("enter second real no. :"))
d=int(input("enter second imaginary no. :"))
if d<0:
    print(c,d,"i")
else:
    print(c,"+",d,"i")
sum_r=a+c
sum_i=b+d
if sum_i<0:
    print("sum is : ",sum_r,sum_i,"i")
else:
    print("sum is : " ,sum_r,"+",sum_i,"i")