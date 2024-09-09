from sql_connect import *
import time

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
            #Add the currency api for seamless conversion and realtime rate where the currency selected 
        #from the api would return a symbol which would be used to search for the currency and return it 
        #to the api and get the exchange rate for it
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
