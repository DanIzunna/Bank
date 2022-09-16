import time
from sql_connect import *

def deposit(acc_no):
    time.sleep(0.5)
    deposit_amt = float(input('Enter a deposit amount: '))
    time.sleep(0.5)
    print('Crediting your account...')

    sql_select = "select * from customers"
    cursor.execute(sql_select)
    records = cursor.fetchall()
    for i in records:
        balance = i[8]
        currency = i[9]

    new_balance = deposit_amt + balance
    increase_balance_sql = "update customers set balance = %s where account_number = %s"%(new_balance, acc_no)
    cursor.execute(increase_balance_sql)
    mydb.commit()
    time.sleep(1.0)
    print('Successfully deposited '+ currency +'{:,.2f}'.format(deposit_amt) + ' into your account')