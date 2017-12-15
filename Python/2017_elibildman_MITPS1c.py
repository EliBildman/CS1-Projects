init_balance = float(input("Outstanding balance: "))
interest = float(input("Annual interest rate (dec): "))
balance = 1
upper_bound = (init_balance * (1 + (interest / 12.0)) ** 12.0) / 12.0
lower_bound = init_balance / 12.0
monthly_payment = (upper_bound + lower_bound) / 2

while abs(balance) >= .005:
    balance = init_balance
    for month in range(12):
        balance = balance * (1 + (interest / 12))
        balance = balance - monthly_payment
    if balance > 0:
        lower_bound = monthly_payment
        monthly_payment = (upper_bound + monthly_payment) / 2
    elif balance < 0:
        upper_bound = monthly_payment
        monthly_payment = (lower_bound + monthly_payment) / 2

monthly_payment = round(monthly_payment, 2)

print("Monthly payment:", monthly_payment)
