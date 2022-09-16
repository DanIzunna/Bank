import time
from register import Register
from sign_in import SignIn

class Bank:
    
    def __str__(self):
        return 'A Bank App'

    def operation():
        print('WELCOME TO BIZ BANK LTD.')
        time.sleep(0.5)
        print('\tPress 1 to Register')
        time.sleep(0.5)
        print('\tAlready have an account, \nPress 2 to Login\n Press Enter To exit ')
        user_choice = input('Enter here: ')
        if user_choice == '1':
            return Register.register()
        elif user_choice == '2':
            return SignIn.log_in()
        elif user_choice == '':
            print('Logging out... ')
            time.sleep(1.0)
            exit('Closing...')
        else:
            print('Invalid Input!!')
            return Bank.operation()
        