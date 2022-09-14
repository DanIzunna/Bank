import random
import datetime
from datetime import date
import time
import hashlib
import mysql.connector
from current_acc import Current_Account
from savings_acc import Savings_Account
from fixed_deposit import Fixed_Deposit_Account
# Linking to the database
mydb = mysql.connector.connect(user="Jon",passwd="ilikecheeseballs2",host="localhost",database ='BANK', auth_plugin= 'mysql_native_password' ) 
cursor = mydb.cursor()

class Bank:
    
    def __str__(self):
        return 'A Bank App'
    #Creating the methods in the class
    # Move register to a separate file
    def register():
        print('WELCOME TO BIZ BANK LTD.')
        time.sleep(0.5)
        first_name = input('Please Enter your First Name: ')
        time.sleep(0.5)
        last_name = input('Please Enter your  Last Name: ')
        time.sleep(0.5)
        date_of_birth = Bank.date_of_birth()
        time.sleep(0.5)
        gender = Bank.gender_check()

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
        time.sleep(2.0)

        # Creating a pin and hashing it to store in the database
        print('Create a PIN')
        pin = Bank.pin_check()
# Select account type...Savings or Current or Fixed deposit 
        account_type_ = input('Select an account type:\n\t1. Current Account\n\t2. Savings Account\n\t3. Fixed Deposit Account\n')   
        if account_type_ == '1':
            account_type = 'Current Account'
            balance = Current_Account.initial_deposit()
            # print(Current_Account.deposit())
        elif account_type_ == '2':
            account_type = 'Savings Account'
            balance =Savings_Account.deposit()
        elif account_type_ == '3':
            account_type = 'Fixed Deposit Account'
            balance = Fixed_Deposit_Account.deposit()
        else:
            return ('Invalid')
        currency = 'NGN'
        # currency = Current_Account.currency_format()
    # Saving new customer to database
        sql = "INSERT INTO CUSTOMERS(FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, GENDER, ACCOUNT_NUMBER, PIN, ACCOUNT_TYPE, DATE_CREATED, CURRENCY, BALANCE) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        vals = (first_name, last_name, date_of_birth, gender, account_number, pin, account_type, date_created, currency, balance)
        cursor.execute(sql, vals)
        mydb.commit()
        return ('Account Successfully created')
        
# Split amount by comma to prevent errors when comma is used to separate numbers

# To use try except to exit when enter is pressed

    def gender_check():
        #To ensure that gender is male or female
        gender_ = input('Please Select your Gender \n\tMale (M)\n\tFemale (F)\n ').upper()
        if gender_ not in ['M', 'F', 'MALE', 'FEMALE']:
            time.sleep(0.5)
            print('INVALID GENDER\n MUST BE EITHER MALE OR FEMALE')
            return Bank.gender_check()
        elif gender_ == 'MALE':
                gender_ = 'M'
        elif gender_ == 'FEMALE':
            gender_ = 'F'
        return gender_


# Make password confirmation
    def pin_check():
        raw_pin = (input('Create your FOUR digit secret PIN: '))
        if raw_pin.isnumeric() == True and len(raw_pin) == 4:
            raw_pin = int(raw_pin)
        # Hashing the pin for enhanced security
            pin_hash = str(raw_pin)
            encoded=pin_hash.encode()
            pin = hashlib.sha256(encoded).hexdigest()
        else:
            print('Invalid !!\nMust be four digits only!!'.upper())
            return Bank.pin_check()
        return pin

    def date_of_birth():
        # To implement the most appropriate later
        # y = int(input('Enter your year of birth: '))
        # m = int(input('Enter your month of birth: '))
        # d = int(input('Enter your day of birth: '))

        try:
            dob = input('Enter your date of birth YYYY-MM-DD: ')
            dob = date.fromisoformat(dob)
            today_date = date.fromisoformat(str(date.today()))
            if (today_date.year - dob.year) < 18:
                print('Too young ')
            else:
                dob = dob
            return dob
        except ValueError:
            print('Invalid date of birth')
            return Bank.date_of_birth()
    

        

# Fixed deposit you select withdrawal date...And the interest rate is 2.1% for 30 days...
# To deposit in fixed account you need to select the duration


print(Bank.register())