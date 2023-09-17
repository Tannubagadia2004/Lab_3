# To calculate tax
salary=int(input("Enter gross salary : "))
if salary<300000:
    print("No tax")
elif 300000<salary<1000000:
    print(salary*0.1,"tax to be paid")
elif 100000<salary<2500000:
    print(salary*0.2,"tax to be paid")
elif salary>250000:
    print(salary*0.3,"tax to be paid")