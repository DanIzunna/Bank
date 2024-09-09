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

        '''#!/usr/bin/python

"""
Usage:
    currency_converter.py [--amount=<amount>] [--input_currency=<input_currency>] [--output_currency=<output_currency>] 

Options:
    --amount=<amount>                       Amount
    --input_currency=<input_currency>       inputCurrency
    --output_currency=<output_currency>     outputCurrency
"""

from docopt import docopt
import json
import requests
import re

with open('currency_code.json') as data_file:    
    currency_code = json.load(data_file)
    
def check_currency_code(currency_code, currency, total_code):
    for i in range(total_code):
        if unicode(currency, "utf-8") == currency_code['code'][i]['symbol']:
            currency = currency_code['code'][i]['letter']
            break
    return currency

def convert_currency(input_currency, output_currency, amount):
    r = requests.get('https://www.google.com/finance/converter?a={}&from={}&to={}'.format(amount, input_currency, output_currency))
    if r.status_code == 200:
        data = r.content
        try:
            fetch_result = re.findall ('<span class=bld>(.*?) '+output_currency+'</span>', data, re.DOTALL )
            conversion_result = float("".join(fetch_result).replace('\n',' '))
            return conversion_result
        except:
            return 'enter another output currency'
    else:
        return 'try again later'

def main():
    arguments = docopt(__doc__)
    amount = arguments.get('--amount')
    input_currency = arguments.get('--input_currency')
    output_currency = arguments.get('--output_currency')

    total_code =  len(currency_code['code'])
    if input_currency.isalpha() == False or len(input_currency) < 3:
        input_currency = check_currency_code(currency_code, input_currency , total_code)
    result = {
        "input": {
            "amount": amount,
            "currency": str(input_currency)
        },
        "output": {
        }
    }
    if output_currency:
        if output_currency.isalpha() == False or len(output_currency) < 3:
            output_currency = check_currency_code(currency_code, output_currency , total_code)
        conversion_result = convert_currency(input_currency, output_currency, amount)
        result['output'].update({str(output_currency): conversion_result})
        print json.dumps(result, sort_keys=True, indent=4)
    else:
        for i in range(total_code):
            output_currency = currency_code['code'][i]['letter']
            if output_currency != input_currency:
                conversion_result = convert_currency(input_currency, output_currency, amount)
                result['output'].update({str(output_currency): conversion_result})
        print json.dumps(result, sort_keys=True, indent=4)


if __name__ == '__main__':
    main()'''
        #Latest update for converter
        
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
