print("Hal pyramid Pattern of dollar (*): ")
n = int(input("Enter number of rows"))
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)