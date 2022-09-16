import time
from sql_connect import *

def check_balance(acc_no):
    try:
        time.sleep(1.0)
        print('To view balance, 1% would be deducted as service fee')
        time.sleep(0.5)
        print('\tPress 1 to Proceed \n\tPress 0 to exit\n\tPress 9 to go to the previous Menu')
        time.sleep(0.4)
        confirm = int(input('Enter Here: '))
        
        sql_select = "select * from customers where account_number = %s"%acc_no
        cursor.execute(sql_select)
        records = cursor.fetchall()
        for i in records:
            balance = i[8]
            currency = i[9]
        
        new_balance = balance - (balance * 0.001)
        if confirm == 1:
            time.sleep(0.5)
            print('Your account balance is '+ currency+ '{:,.2f}'.format(balance))
            change_balance_sql = "update customers set balance = %s where account_number = %s"%(new_balance, acc_no)
            cursor.execute(change_balance_sql)
            mydb.commit()
            time.sleep(1.0)
            print('Charges deducted')
            time.sleep(1.0)
            print('Your new account balance is '+ currency+ '{:,.2f}'.format(new_balance))
        elif confirm == 0:
            exit('Logging Out')
        elif confirm == 9:
            print('Going Back...')
    except ValueError:
        print('Enter only the specified numbers')
        return check_balance(acc_no)