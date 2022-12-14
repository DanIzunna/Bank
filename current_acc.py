import time
from sql_connect import *
from check_balance import check_balance
from deposit import deposit
from withdraw import withdraw
from transfer import transfer
from change_pin import change_pin
from delete_account import delete_account

class Current_Account:
    def __str__(self):
        return 'Current Account'

    # Creating the functionalities of current account
    
    def initial_deposit():
        try:
            deposit_amt = float(input('Enter a deposit amount NGN N: '))
            if deposit_amt < 10000:
                print('Deposit too low!!')
                return Current_Account.initial_deposit()
            else:
                print('Successfully deposited N{:,.2f}'.format(deposit_amt)+ 'into the account')
            return deposit_amt
        except ValueError:
            print('Invalid amount\nAmount must be numbers only!!')
            return Current_Account.initial_deposit()
    
    def operation(acc_no):
        try:
            time.sleep(1.0)
            print('What do you want to do\n\t1. View Balance\n\t2. Withdraw Funds \n\t3. Deposit Funds \n\t4. Convert Currency \n\t5. Transfer Funds \n\t6. Change Pin \n\t7. Close Account \nPress Enter to Logout')
            choice = (input('What do you want to do? '))
            if choice == '1':
                check_balance(acc_no)
                return finish(acc_no)   
            elif choice == '2':
                withdraw(acc_no)
                return finish(acc_no)
            elif choice == '3':
                deposit(acc_no)
                return finish(acc_no)
            elif choice == '4':
                Current_Account.currency_converter(acc_no)
            elif choice == '5':
                transfer(acc_no)
                return finish(acc_no)
            elif choice == '6':
                change_pin(acc_no)
                return finish(acc_no)
            elif choice == '7':
                delete_account(acc_no)
            elif choice == '':
                exit('Logging Out...')
        except ValueError:
            print('Invalid Input...\nEnter an available operation')
            return Current_Account.operation(acc_no)

# Do you want to perform another transaction? make it a function called finish....yes or no
def finish(acc_no):
    another = input('Do you want to perform another transaction?\n\t\tY / N\n').upper()
    if another == 'Y':
        time.sleep(0.5)
        print('Loading...')
        time.sleep(0.5)
        return Current_Account.operation(acc_no)
    elif another == 'N':
        time.sleep(0.5)
        exit('Signing Out...')
    else:
        print('Invalid Input!!')
        return finish(acc_no)
