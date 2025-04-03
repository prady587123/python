print("Enter a number (Numerator) : ")
num = int(input())
print("Enter a number (Denominator): ")
no = int(input())36
if num%no == 0:
    print ("\n" + str (num) + " is divisible by " + str(no))
else:
    print ("\n" +str(num) + " is not divisible by" +str(no))