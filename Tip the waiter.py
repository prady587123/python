def total_calc(bill_amount, tip_perc):
    total = bill_amount*(1+0.1*tip_perc)
    total = round(total,2)
    print(f"Please pay ₹{total}")
total_calc(150,20)