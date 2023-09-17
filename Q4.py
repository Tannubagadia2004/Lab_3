# sum is divisible by 3 or not.
num=int(input("Enter number :"))
sum=0
while 99<num<1000:
    a=num%10
    sum=sum+a
    num=num//10
if sum%3==0:
    print(sum,"is divisible by 3")
else:
    print(sum,"is not divisible by 3")
