import time
import mysql.connector
mydb = mysql.connector.connect(user="Jon",passwd="ilikecheeseballs2",host="localhost",database ='BANK', auth_plugin= 'mysql_native_password' ) 
cursor = mydb.cursor()

def deposit(balance, acc_no):
    time.sleep(0.5)
    deposit_amt = float(input('Enter a deposit amount: '))
    time.sleep(0.5)
    print('Crediting your account...')
    new_balance = deposit_amt + balance
    increase_balance_sql = "update customers set balance = %s where account_number = %s"%(new_balance, acc_no)
    cursor.execute(increase_balance_sql)
    mydb.commit()
    time.sleep(1.0)
    print('Successfully deposited N%s into the account'%deposit_amt)
    return 'Done'