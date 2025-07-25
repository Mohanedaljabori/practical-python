# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    total_months += 1

    if extra_payment_start_month <= total_months <= extra_payment_end_month:
        monthly_payment = payment + extra_payment
    else :
        monthly_payment = payment

    principal = principal * (1+rate/12) - monthly_payment

    if principal < 0:
        monthly_payment += principal
        principal = 0

    total_paid += monthly_payment

    print(total_months, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2), 
      '\nTotal months', total_months)