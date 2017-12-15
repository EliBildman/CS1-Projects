balance = float(input("Outstanding balance: "))
interest = float(input("Annual interest rate (dec): "))
minpay = float(input("Minimum monthly payment rate (dec): "))

paid = 0
for month in range(12):
    print("Month: ", month + 1)
    payment = round(balance * minpay, 2)
    intpay = round((interest / 12) * balance, 2)
    principle = round(payment - intpay, 2)
    balance = round(balance - principle, 2)
    paid = round(paid + payment, 2)
    print("Payment: ", payment)
    print("Principle paid: ", principle)
    print("Remaining balance: ", balance)
    print()

print("Total paid: ", paid)
print("Remaining balance: ", balance)
