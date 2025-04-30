import calendar

year = int(input("Enter the year:"))
month = int(input("Enter the month(1-12) :"))

if month < 1 or month > 12:
    print ("Invalid month. Please enter no between  and 12.")
else:
    cal = calendar.month(year, month)
    print("Calender for{}-{}".format(year,month))
    print(cal)