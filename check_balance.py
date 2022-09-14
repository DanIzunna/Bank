import time
import mysql.connector
mydb = mysql.connector.connect(user="Jon",passwd="ilikecheeseballs2",host="localhost",database ='BANK', auth_plugin= 'mysql_native_password' ) 
cursor = mydb.cursor()

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
        print('Your account balance is '+ currency+ '{:,.2f}'.format(new_balance))
        change_balance_sql = "update customers set balance = %s where account_number = %s"%(new_balance, acc_no)
        cursor.execute(change_balance_sql)
        mydb.commit()
        time.sleep(1.7)
        print('Charges deducted')
        time.sleep(1.7)
        return 'Your new account balance is '+ currency+ '{:,.2f}'.format(new_balance)
    elif confirm == 0:
        exit('Logging Out')
    elif confirm == 9:
        return 'Going Back'