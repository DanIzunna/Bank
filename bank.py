import time
from register import Register
from sign_in import SignIn

class Bank:
    
    def __str__(self):
        return 'A Bank App'

    def operation():
        try:
            print('WELCOME TO THE TRUST BANK ')
            time.sleep(0.5)
            print('\tPress 1 to Register')
            time.sleep(0.5)
            print('\tAlready have an account, Press 2 to Login\n\tPress Enter To exit ')
            user_choice = input('Enter here: ')
            if user_choice == '1':
                print( Register.register())
                return Bank.operation()
            elif user_choice == '2':
                return SignIn.log_in()
            elif user_choice == '':
                print('Logging out... ')
                time.sleep(1.0)
                exit('Closing...')
            else:
                print('Invalid Input!!')
                return Bank.operation()
        except KeyboardInterrupt:
            print('\nSigning Out...')
            time.sleep(0.5)
            print('Closed')

Bank.operation()