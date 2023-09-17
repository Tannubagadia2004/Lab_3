# To find greatest number
num_1=int(input("Enter number-1 :"))
num_2=int(input("Enter number-2 :"))
num_3=int(input("Enter number-3 :"))
if num_1>num_2:
    if num_1>num_3:
        print(num_1,"is greater")
    else:
        print(num_3,"is greater")
elif num_2>num_3:
    print(num_2,"is greater")
else:
    print(num_3,"is greater")
    
