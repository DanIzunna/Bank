import time
from current_acc import Current_Account
from sql_connect import *
from pin_check import pin_check

# Creating the class
class SignUp:
    trials = 3
    @classmethod
    def attempts(cls):
        cls.trials -= 1
        if cls.trials == 0:
            quit('Profile Locked')

    # Function to sign in
    def log_in():
        print('Sign in with your account number\n'.upper())
        time.sleep(1.0)
        acc_no = int(input('Enter your Account Number: '))
        # Comparing with the database accounts
        sql_select = "select * from customers where account_number = %s"%acc_no
        cursor.execute(sql_select)
        records = cursor.fetchall()

        if str(acc_no) not in str(records):
            SignUp.attempts()
            print('Invalid account number!!')
            time.sleep(1.0)
            print('\nYou have %s trials remaining\n'%SignUp.trials)
            time.sleep(1.5)
            return SignUp.log_in()
            
        for i in records:
            account_number=i[6]
            if str(acc_no) in str(account_number):
                pin = pin_check()
                if str(pin) in str(i):
                    time.sleep(0.5)
                    print('Successfully signed in')
                    time.sleep(0.5)
                    print('\tWelcome %s, %s\n\tAccount Type: %s'%(i[1], i[2], i[7]))
                    balance = i[8]
                    currency = i[9]
                    if i[7] == 'Current Account':
                        return Current_Account.operation(acc_no)
                    # elif i[7] == 'Savings Account':
                    #     return Savings_Account.operation()
                    # else:
                    #     return Fixed_Deposit_Account.operation()
                    
                else:
                    print('Incorrect Pin!!')
                    time.sleep(0.5)
                    print('\nRestart Your Login')
                    SignUp.log_in()
                        
SignUp.log_in()
