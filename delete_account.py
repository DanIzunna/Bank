import time
from sql_connect import *
from pin_check import pin_check

#The classmethod to track the number of wrong attempts
class Delete_Acc:
    trials = 3
    @classmethod
    def attempts(cls):
        cls.trials -= 1
        if cls.trials == 0:
            quit('Profile Locked')

# Pin confirmation and delete
def pin_confirm(acc_no, saved_pin):
    confirm_pin = pin_check()
    if confirm_pin == saved_pin:
        delete_sql = "DELETE FROM customers WHERE account_number = %s and pin = '%s'"%(acc_no, confirm_pin)
        cursor.execute(delete_sql)
        mydb.commit()
        time.sleep(1.0)
        print('Deleting your data from our systems....')
        time.sleep(1.5)
        print('Please wait a Moment....')
        time.sleep(2.0)
        print('Deleting your transaction history....')
        time.sleep(3.0)
        print('Successfully Deleted your account')
        time.sleep(1.0)
        quit('Goodbye...')
    else:
        print('Incorrect pin!!')
        Delete_Acc().attempts()
        print('You have %s trials remaining'% Delete_Acc.trials)
        pin_confirm(acc_no, saved_pin)

# The main delete account function
def delete_account(acc_no):
    sql_select = "select * from customers where account_number = %s"%acc_no
    cursor.execute(sql_select)
    records = cursor.fetchall()
    for i in records:
        saved_pin = i[5]
        first_name = i[1]
        last_name = i[2]
    confirm = input('%s %s Are you sure you want to delete your account?\n\t\tY / N\n'%(first_name, last_name)).upper()
    if confirm == 'Y':
        pin_confirm(acc_no, saved_pin)

   