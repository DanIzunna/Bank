import hashlib
import time
import mysql.connector
from current_acc import Current_Account

# Connecting to the database
mydb = mysql.connector.connect(user="Jon",passwd="ilikecheeseballs2",host="localhost",database ='BANK', auth_plugin= 'mysql_native_password' ) 
cursor = mydb.cursor() 

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

        if str(acc_no)  not in str(records):
            SignUp.attempts()
            print('Invalid account number!!')
            time.sleep(1.0)
            print('\nYou have %s trials remaining\n'%SignUp.trials)
            time.sleep(1.5)
            return SignUp.log_in()
            
        for i in records:
            # print(j)
            if str(acc_no) in str(i):
                pin = SignUp.pin_check()
                if str(pin) in str(i):
                    time.sleep(0.5)
                    print('Successfully signed in')
                    time.sleep(0.5)
                    print('\tWelcome %s, %s\n\tAccount Type: %s'%(i[1], i[2], i[7]))  # print('\tWelcome '+str(i[1])+', '+ str(i[2]))
                    balance = i[8]
                    currency = i[9]
                    if i[7] == 'Current Account':
                        return Current_Account.operation(balance, acc_no, currency)
                    # elif i[7] == 'Savings Account':
                    #     return Savings_Account.operation()
                    # else:
                    #     return Fixed_Deposit_Account.operation()
                    print()

                else:
                    print('Incorrect Pin!!')
                    time.sleep(0.5)
                    print('\nRestart Your Login')
                    SignUp.log_in()
                        
    def pin_check():
        raw_pin = (input('Enter your FOUR digit PIN: '))
        if raw_pin.isnumeric() == True and len(raw_pin) == 4:
            raw_pin = int(raw_pin)
        # Hashing the pin for enhanced security
            pin_hash = str(raw_pin)
            encoded=pin_hash.encode()
            pin = hashlib.sha256(encoded).hexdigest()
        else:
            print('Invalid !!\nMust be four digits only!!'.upper())
            return SignUp.pin_check()
        return pin

SignUp.log_in()


    # sign_in()
    # if trials == 0:
    # # time.sleep(2.0)
    #     exit('Try again Later')
    # else:
    #     continue