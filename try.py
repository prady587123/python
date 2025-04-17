try:
    number = int(input("Enter a number :"))
    print("The numbeer entered is:" , number)
except ValueError as ex:
    print("Exception occured:" , ex)