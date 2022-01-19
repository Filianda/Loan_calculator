import math
def user_inputs():
    monthly_payment = 0
    months_number = 0
    loan_principal = int(input('Loan principal: '))
    payments_category = input('What do you want to calculate?\ntype "m" - for number of monthly payments,\ntype "p" - for the monthly payment:\n')
    if payments_category == 'm':
        monthly_payment = int(input('Enter the monthly payment:\n'))
    elif payments_category == 'p':
        months_number = int(input('Enter the number of months:\n'))
    return [monthly_payment,months_number,loan_principal, payments_category]

def calculator(monthly_payment,months_number,loan_principal, payments_category):
    if payments_category == 'm':
        months_number = math.ceil(loan_principal/monthly_payment)
        if months_number == 1:
            month_form = 'month'
        else:
            month_form = 'months'
        print(f'\nIt will take {months_number} {month_form} to repay the loan')
    else:
        monthly_payment = math.ceil(loan_principal/months_number)
        last_payment = loan_principal - (months_number - 1) * monthly_payment
        if monthly_payment == last_payment:
            print(f'\nYour monthly payment = {monthly_payment}')
        else:
            print(f'\nYour monthly payment = {monthly_payment} and the last payment = {last_payment}')
    return [months_number,monthly_payment]

def main():
    user_paramiters = user_inputs()
    monthly_payment = user_paramiters[0]
    months_number = user_paramiters[1]
    loan_principal = user_paramiters[2]
    payments_category = user_paramiters[3]
    calculator(monthly_payment,months_number,loan_principal, payments_category)

main()
