rows = int(input("please enter total number of rows"))
number = 1
print("Floyed's Triangle")
for i in range(1, rows+1):
    for j in range(1, i+1) :
        print(number, end=" ")
        number = number + 1
    print()