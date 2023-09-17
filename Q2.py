# calculate BMI
weight=float(input("Enter weight (in gram) :"))
height=float(input("Enter height(in cm) :"))
w_new=weight*0.001    #converting weight in kg
h_new=height*0.01      #converting height in m
bmi=w_new/h_new
print("BMI is : ",bmi)