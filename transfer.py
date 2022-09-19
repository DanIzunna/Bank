from sql_connect import *
import time
from pin_check import pin_check

def transfer(acc_no):
    try:
        time.sleep(1.0)
        print('Do You want to transfer funds?'.title())
        time.sleep(0.5)
        print('\tPress 1 to Proceed \n\tPress 0 to exit\n\tPress 9 to go to the previous Menu')
        time.sleep(0.5)
        confirm = int(input('Enter Here: '))
        
        sql_select = "select * from customers where account_number = %s"%acc_no
        cursor.execute(sql_select)
        records = cursor.fetchall()
        for i in records:
            balance = i[8]
            saved_pin = i[5]
            first_name = i[1]
            last_name = i[2]
            currency = i[9]

        if confirm == 1:
            time.sleep(0.5)
            amount = float(input('Enter the Amount you want to Transfer: '))
            if balance > amount:
                time.sleep(0.5)
                recepient_acc = int(input("Enter the Recipient's Account Number: "))
                sql_select = "select * from customers where account_number = %s"%recepient_acc
                cursor.execute(sql_select)
                record = cursor.fetchall()
                for i in record:
                    recepient_balance = i[8]
                    recepient_first_name = i[1]
                    recepient_last_name = i[2]

                if acc_no == recepient_acc:
                    time.sleep(0.5)
                    print('You cannot transfer to yourself!!!')
                    return transfer(acc_no)

                elif str(recepient_acc) not in str(record):
                    time.sleep(0.5)
                    print('Invalid Account Number!!')
                    return transfer(acc_no)

                else:
                    time.sleep(1.0)
                    print('%s %s You are about to transfer %s{:,.2f}'.format(amount)%(first_name, last_name, currency) +' to %s %s'%(recepient_first_name,recepient_last_name))
                
                    pin_verification = pin_check()

                    if pin_verification == saved_pin:
                        new_balance = balance - amount
                        change_balance_sql = "update customers set balance = %s where account_number = %s"%(new_balance, acc_no)
                        cursor.execute(change_balance_sql)
                        mydb.commit()
                        
                        update_balance =  recepient_balance + amount
                        recipient_balance_sql = "update customers set balance = %s where account_number = %s"%(update_balance, recepient_acc)
                        cursor.execute(recipient_balance_sql)
                        mydb.commit()
                        time.sleep(1.5)
                        print('Successfully Transferred %s{:,.2f}'.format(amount)%currency +' to %s %s'%(recepient_first_name, recepient_last_name))
                    
                    else:
                        time.sleep(1.0)
                        print('Invalid PIN!!!')
                        return transfer(acc_no)
            elif balance == amount:
                time.sleep(1.0)
                print('You cannot transfer all your money!!')
                return transfer(acc_no)
            else:
                time.sleep(1.0)
                print('Balance too low!!')
                return transfer(acc_no)
                        
        elif confirm == 0:
            exit('Logging Out')
        elif confirm == 9:
            print('Going Back...')
        else:
            print('Invalid Input!!')
            return transfer(acc_no)

    except ValueError:
        print('Invalid!!')
        return transfer(acc_no)
        
# Charges for transferring funds