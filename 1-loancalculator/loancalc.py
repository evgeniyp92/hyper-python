from math import ceil, log, floor
import argparse


def calculate_monthly_payment(principal, interest, periods):
    monthly_interest = interest / 1200
    payment = principal * (
            (monthly_interest * (1 + monthly_interest) ** periods) / ((1 + monthly_interest) ** periods - 1))
    payment = ceil(payment)
    print(f'Your monthly payment = {payment}!')
    return payment


def calculate_principal(periods, interest, payment):
    monthly_interest = interest / 1200
    principal = payment / (
            (monthly_interest * (1 + monthly_interest) ** periods) / ((1 + monthly_interest) ** periods - 1))
    principal = floor(principal)
    print(f'Your loan principal = {principal}!')
    return principal

def calculate_overpayment(principal, interest, periods):
    overpayment = calculate_monthly_payment(principal, interest, periods) * periods - principal
    print(f'Overpayment = {int(overpayment)}')
    return overpayment


def calculate_time_to_repay(principal, interest, payment):
    monthly_interest = interest / 1200
    num_payments = ceil(-log(1 - (monthly_interest * principal / payment)) / log(1 + monthly_interest))
    years = num_payments // 12
    months = num_payments % 12
    overpayment = calculate_overpayment(principal, interest, num_payments)
    print(overpayment)
    print(f'It will take {years} years and {months} months to repay this loan!') if years else print(f'It will take '
                                                                                                     f'{months} months '
                                                                                                     f'to repay this '
                                                                                                     f'loan!')


def calculate_diff_payments(principal, periods, interest):
    monthly_interest = interest / 1200
    overpayment = 0
    for i in range(periods):
        payment = ceil((principal / periods) + (monthly_interest * (principal - ((principal * i) / 10))))
        overpayment += payment - (principal / periods)
        print(f'Month {i + 1}: payment is {payment}')
    print()
    print(f'Overpayment = {int(overpayment)}')


def check_no_negatives(args):
    attributes = [args.principal, args.periods, args.interest, args.payment]
    for attribute in attributes:
        if attribute is not None and float(attribute) < 0:
            return False
    return True


# Set up CLI argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')
parser.add_argument('--type', choices=['diff', 'annuity'], help='Incorrect parameters')

# Get the list of args and cast the values into the right types
args = parser.parse_args()

if args and check_no_negatives(args):
    if args.type == 'diff':
        # differentiated payment math
        if (args.principal and args.periods and args.interest) and not args.payment:
            calculate_diff_payments(int(args.principal), int(args.periods), float(args.interest))
        else:
            print('Incorrect parameters')
    elif args.type == 'annuity':
        # annuity payment math
        if (args.principal and args.periods and args.interest) and not args.payment:
            calculate_monthly_payment(int(args.principal), float(args.interest), int(args.periods))
        if (args.periods and args.interest and args.payment) and not args.principal:
            calculate_principal(int(args.periods), float(args.interest), float(args.payment))
        if (args.principal and args.interest and args.payment) and not args.periods:
            calculate_time_to_repay(int(args.principal), float(args.interest), float(args.payment))
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
