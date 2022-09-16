import time
from sql_connect import *

def withdraw(acc_no):
    withdraw_amount = float(input('Enter the amount you want to withdraw: '))
    sql_select = "select * from customers"
    cursor.execute(sql_select)
    records = cursor.fetchall()
    for i in records:
        balance = i[8]
        currency = i[9]
    confirm = input('Are you sure you want to withdraw '+currency + '{:,.2f}'.format(withdraw_amount)+'\n\t\tY / N?\n ').upper()
    if confirm == 'Y':
        if balance - withdraw_amount <= 0:
            time.sleep(1.0)
            print('Insufficient balance')
        elif (balance - withdraw_amount) < (0.01* balance):
            time.sleep(1.0)
            print('Balance too low')
            time.sleep(0.5)
            print('You cannot withdraw everything in your account')
        else:
            balance = (balance - withdraw_amount)
            withdraw_sql = "update customers set balance = %s where account_number = %s"%(balance, acc_no)
            cursor.execute(withdraw_sql)
            mydb.commit()
            time.sleep(0.5)
            print('Transaction Completed Successfully')
    else:
        time.sleep(0.5)