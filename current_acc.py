import math
import time
import mysql.connector
   
mydb = mysql.connector.connect(user="Jon",passwd="ilikecheeseballs2",host="localhost",database ='BANK', auth_plugin= 'mysql_native_password' ) 
cursor = mydb.cursor() 

class Current_Account():
    def __str__(self):
        return 'Current Account'

    # Creating the functionalities of current account
    
    def initial_deposit():
        deposit_amt = float(input('Enter a deposit amount NGN N: '))
        if deposit_amt < 10000:
            print('Deposit too low!!')
            return Current_Account.initial_deposit()
        else:
            print('Successfully deposited N%s into the account'%deposit_amt)
        return deposit_amt
    
    def operation(balance, acc_no, currency):
        print('What do you want to do\n\t1. View Balance\n\t2. Withdraw Funds \n\t3. Deposit Funds \n\t4. Convert Currency \n\t5. Transfer Funds \n\t6. Change Pin \n\t7. Close Account')
        choice = int(input('What do you want to do? '))
        if choice == 1:
            Current_Account.check_balance(balance, acc_no, currency)
        elif choice == 2:
            Current_Account.withdraw(balance, acc_no)
        elif choice == 3:
            Current_Account.deposit(balance, acc_no)
        elif choice == 4:
            Current_Account.currency_converter(balance, acc_no, currency)

    def check_balance(balance, acc_no, currency):
        time.sleep(1.0)
        print('To view balance, 1% would be deducted as service fee')
        time.sleep(0.5)
        print('\tPress 1 to Proceed \n\tPress 0 to exit\n\tPress 9 to go to the previous Menu')
        time.sleep(0.4)
        confirm = int(input('Enter Here: '))
        new_balance = balance - (balance * 0.001)
        if confirm == 1:
            time.sleep(0.3)
            if currency == 'USD':
                currency = '$'
            else:
                currency = 'N'
            print('Your account balance is %s%s'%(currency, balance))
            change_balance_sql = "update customers set balance = %s where account_number = %s"%(new_balance, acc_no)
            cursor.execute(change_balance_sql)
            mydb.commit()
            time.sleep(1.7)
            print('Charges deducted')
            time.sleep(1.7)
            print('Your new account balance is %s%s'%(currency, new_balance))
        elif confirm == 0:
            exit('Logging Out')
        elif confirm == 9:
            Current_Account.operation(balance, acc_no, currency)
        
    def withdraw(balance, acc_no):
        withdraw_amount = float(input('Enter the amount you want to withdraw '))
        confirm = input('Are you sure you want to withdraw N %s Y or N? '%withdraw_amount).upper()
        if confirm == 'Y':
            if balance - withdraw_amount <= 0:
                time.sleep(1.0)
                print('Insufficient balance')
            elif (balance - withdraw_amount) < (0.01* balance):
                time.sleep(1.0)
                print('Balance too low')
                time.sleep(0.5)
                print('You cannot withraw everything in your account')
            else:
                balance = (balance - withdraw_amount) - (balance * 0.001)
                withdraw_sql = "update customers set balance = %s where account_number = %s"%(balance, acc_no)
                cursor.execute(withdraw_sql)
                mydb.commit()
                time.sleep(0.5)
                print('Transaction Completed Successfully')
        else:
            Current_Account.withdraw(balance, acc_no)
        return 'Done'

    def deposit(balance, acc_no):
        time.sleep(0.5)
        deposit_amt = float(input('Enter a deposit amount: '))
        time.sleep(0.5)
        print('Crediting your account...')
        balance = deposit_amt + balance
        increase_balance_sql = "update customers set balance = %s where account_number = %s"%(balance, acc_no)
        cursor.execute(increase_balance_sql)
        mydb.commit()
        time.sleep(1.0)
        print('Successfully deposited N%s into the account'%deposit_amt)
        return 'Done'
        
    def currency_converter(balance, acc_no, currency):
        if currency == 'NGN':
            currency = 'N'
            time.sleep(1.0)
            print('Naira to Dollar Converter')
            time.sleep(1.0)
            convert_amount = float(input('Enter amount to convert: '))
            if balance - convert_amount < 0:
                time.sleep(1.0)
                print('Insufficient balance')
            else:
                new_currency = '$'
                exchange_rate = 0.00185
                balance = convert_amount * exchange_rate
                convert_sql = "update customers set balance = %s where account_number = %s"%(balance, acc_no)
                cursor.execute(convert_sql)
                convert_sql = "update customers set currency = 'USD' where account_number = %s"%(acc_no)
                cursor.execute(convert_sql)
                mydb.commit()
                time.sleep(1.0)
                print('You have successfully converted '+currency + '{:,} '.format(convert_amount)+ 'to '+ new_currency + '{:,.2f}'.format(balance))

        # rectify to have balance if you dont convert all to another currency
        elif currency == 'USD':
            currency = '$'
            time.sleep(1.0)
            print('Dollar to Naira Converter')
            time.sleep(1.0)
            convert_amount = float(input('Enter amount to convert: '))
            if balance - convert_amount <= 0:
                time.sleep(1.0)
                print('Insufficient balance')
            else:
                exchange_rate = 540
                time.sleep(1.0)
                print('Exchange rate is %s'%exchange_rate)
                balance = convert_amount * exchange_rate
                new_currency = 'N'
                convert_sql = "update customers set balance = %s where account_number = %s"%(balance, acc_no)
                cursor.execute(convert_sql)
                mydb.commit()
                convert_sql = "update customers set currency = 'NGN' where account_number = %s"%(acc_no)
                cursor.execute(convert_sql)
                mydb.commit()
                time.sleep(1.0)
                print('You have successfully converted %s%s to %s%s'%(currency, convert_amount, new_currency, balance))

    def transfer(balance, acc_no):
        pass

# Current_Account.currency_converter(balance, acc_no, currency)
# Make the various operations functions

# Do you want to perform another transaction?