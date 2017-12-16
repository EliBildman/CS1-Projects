init_balance = float(input("Outstanding balance: "))
interest = float(input("Annual interest rate (dec): "))
monthly_payment = 0
months = 13

while months > 12:
    months = 0
    monthly_payment += 10
    balance = init_balance
    while balance > 0:
        balance = round(balance * (1 + (interest / 12)), 2)
        balance = round(balance - monthly_payment, 2)
        months += 1
        print(balance)
        if months > 12:
            break

print("Monthly payment:", monthly_payment)
print("Number of months needed", months)
