actual_cost = float(input("Please enter the actual amount of product : "))
sales_amount = float(input("Please enter the sales amount"))
if (sales_amount > actual_cost):
    amount = sales_amount - actual_cost
    print("Total profit ={0}".format (amount) )
else:
    print("no profit")
