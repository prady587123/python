Amount = int (input("Please enter the Amount withdrawn: " ))
note1 = Amount//100
note2 = (Amount%100)//50
note3 =((Amount%100)%50)//10
print("Notes of 100 rupees :", note1)
print("Notes of 50 rupees :", note2)
print("Notes of 10 rupess :" , note3)