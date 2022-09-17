import time
from sql_connect import *
from check_pin import *

def change_pin(acc_no):
    sql_select = "select * from customers where account_number = %s"%acc_no
    cursor.execute(sql_select)
    records = cursor.fetchall()
    for i in records:
        saved_pin = i[5]
        first_name = i[1]
        last_name = i[2]

    confirm = input('%s %s Are you sure you want to change your PIN?( Y / N )\n'%(first_name, last_name)).upper()
    time.sleep(1.0)
    if confirm == 'Y':

        old_pin = input('Enter your old PIN: ')
        time.sleep(1.0)

        if old_pin.isnumeric() == True and len(old_pin) == 4:
            old_pin = int(old_pin)
        # Hashing the pin for comparison with already hashed pin
            pin_hash = str(old_pin)
            encoded = pin_hash.encode()
            old_pin = hashlib.sha256(encoded).hexdigest()
            if old_pin == saved_pin:
                new_pin = pin_check()
                change_pin_sql = "update customers set pin = '%s' where account_number = %s"%(new_pin, acc_no)
                cursor.execute(change_pin_sql)
                mydb.commit()
                print('PIN Successfully updated!')
            
            else:
                print('Incorrect PIN')
                return change_pin(acc_no)
        elif old_pin.isnumeric() != True:
            print('Invalid !!\npin Must be numbers only!!'.upper())

    elif confirm == 'N':
        print('Going Back...')
    else:
        print('Invalid Input!!')
        return change_pin(acc_no)
