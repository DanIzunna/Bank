import time
from sql_connect import *
from check_balance import check_balance
from withdraw import withdraw
from change_pin import change_pin
from delete_account import delete_account

class Fixed_Deposit_Account():
    def __str__(self):
        return 'Fixed Deposit Account'

    def initial_deposit():
        deposit_amt = float(input('Enter a deposit amount NGN: '))
        if deposit_amt < 5000:
            print('Deposit too low!!')
            return Fixed_Deposit_Account.initial_deposit()
        else:
            duration = int(input('Enter the duration of deposit (Years): '))
            # make interest rate automatically generated from deposit amount and time
            interest_rate = 40
            interest = (deposit_amt* interest_rate * duration)/100
            balance = interest + deposit_amt
            time.sleep(1.0)
            print('Interest Rate = '+str(interest_rate)+'%')
            time.sleep(1.0)
            print('Successfully deposited N%s into the account'%deposit_amt)
            time.sleep(1.0)
            print('Your profit of %s will be ready after %s years'%(interest, duration))
        return deposit_amt

    def operation(acc_no):
        try:
            time.sleep(1.0)
            print('What do you want to do\n\t1. View Balance\n\t2. Withdraw Funds \n\t3. Deposit Funds \n\t4. Change Pin \n\t5. Close Account \nPress Enter to Logout')
            choice = (input('What do you want to do? '))
            if choice == '1':
                check_balance(acc_no)
                return finish(acc_no)   
            elif choice == '2':
                withdraw(acc_no)
                return finish(acc_no)
            elif choice == '3':
                deposit(acc_no)
                # Deposit would be changed to initial_deposit since you will need to enter the duration of deposit
                return finish(acc_no)
            elif choice == '4':
                change_pin(acc_no)
                return finish(acc_no)
            elif choice == '5':
                delete_account(acc_no)
            elif choice == '':
                exit('Logging Out...')
        except ValueError:
            print('Invalid Input...\nEnter an available operation')
            return Fixed_Deposit_Account.operation(acc_no)

# Do you want to perform another transaction? make it a function called finish....yes or no
def finish(acc_no):
    another = input('Do you want to perform another transaction?\n\t\tY / N\n').upper()
    if another == 'Y':
        time.sleep(0.5)
        print('Loading...')
        time.sleep(0.5)
        return Fixed_Deposit_Account.operation(acc_no)
    elif another == 'N':
        time.sleep(0.5)
        exit('Signing Out...')
    else:
        print('Invalid Input!!')
        return finish(acc_no)
        
# Fixed deposit you select withdrawal date...And the interest rate is 2.1% for 30 days...
# To deposit in fixed account you need to select the duration
            # To make interrest rate dynamically generated based on the amount deposited and the duration
#Fixed_Deposit_Account.initial_deposit()