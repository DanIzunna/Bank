import datetime
import random
import time
import hashlib
from date_of_birth import date_of_birth_check
from gender_check import gender_check
from current_acc import Current_Account
from savings_acc import Savings_Account
from fixed_deposit import Fixed_Deposit_Account
# Linking to the database
from sql_connect import *

class Register:

    def __str__(self):
        return 'To register for the bank app'

    def register():

        first_name = input('Please Enter your First Name: ')
        time.sleep(0.5)
        last_name = input('Please Enter your  Last Name: ')
        time.sleep(0.5)
        date_of_birth = date_of_birth_check()
        time.sleep(0.5)
        gender = gender_check()

        time.sleep(1.0)
        print('Generating Account Number...')
        time.sleep(1.5)
        print('Please Stand by...')
        account_number = random.randrange(2, 10000000)
        account_number = 270000000+ account_number
        time.sleep(1.0)
        print('Your Account number is %s'%account_number)

        # Storing the date created in db
        date_created = datetime.date.today()

        # Creating a pin and hashing it to store in the database
        time.sleep(2.0)
        print('Create a PIN')
        pin = Register.pin_check()
        # Select account type...Savings or Current or Fixed deposit 
        account_type_ = input('Select an account type:\n\t1. Current Account\n\t2. Savings Account\n\t3. Fixed Deposit Account\n')   
        if account_type_ == '1':
            account_type = 'Current Account'
            balance = Current_Account.initial_deposit()
            # print(Current_Account.deposit())
        elif account_type_ == '2':
            account_type = 'Savings Account'
            balance = Savings_Account.deposit()
        elif account_type_ == '3':
            account_type = 'Fixed Deposit Account'
            balance = Fixed_Deposit_Account.deposit()
        else:
            return ('Invalid')
        currency = 'NGN'

    # Saving new customer to database
        sql = "INSERT INTO CUSTOMERS(FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, GENDER, ACCOUNT_NUMBER, PIN, ACCOUNT_TYPE, DATE_CREATED, CURRENCY, BALANCE) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        vals = (first_name, last_name, date_of_birth, gender, account_number, pin, account_type, date_created, currency, balance)
        cursor.execute(sql, vals)
        mydb.commit()
        return ('Account Successfully created')

#Make password confirmation
    def pin_check():
        raw_pin = (input('Create your FOUR digit secret PIN: '))
        if raw_pin.isnumeric() == True and len(raw_pin) == 4:
            raw_pin = int(raw_pin)
            # Hashing the pin for enhanced security
            pin_hash = str(raw_pin)
            encoded=pin_hash.encode()
            pin = hashlib.sha256(encoded).hexdigest()

        elif raw_pin.isnumeric() != True:
            print('Invalid !!\npin Must be numbers only!!'.upper())
            return pin_check()

        elif raw_pin.isnumeric() == True and len(raw_pin) > 4:
            print('Invalid !!\npin Must be four digits only!!'.upper())
            return pin_check()
        return pin


Register.register()