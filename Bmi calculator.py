height = float(input("Enter your height in CM :"))
weight = float (input("Enter your weight in KG :"))
BMI = weight/(height/100)**2
print("Your BMI is", BMI)
if BMI <= 18.4:
    print("your are under weight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are over weight")
elif BMI <= 34.9:
    print("you are severly over weight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print ("You are severly obese")

