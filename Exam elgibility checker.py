medical_cause = input("Did you have any medical cause? Y/N :")
atten = int(input("Enter the attendence of the student :"))
if medical_cause == "Y":
    print("You are allowed") 
else :
  if atten >= 75:
     print("You are allowed to write the exam")
  else : 
     print ("You are NOT allowed to write the exam")
