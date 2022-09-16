import datetime
from datetime import date

def date_of_birth_check():
    # To implement the most appropriate later
    # y = int(input('Enter your year of birth: '))
    # m = int(input('Enter your month of birth: '))
    # d = int(input('Enter your day of birth: '))

    try:
        dob = input('Enter your date of birth YYYY-MM-DD: ')
        dob = date.fromisoformat(dob)
        today_date = date.fromisoformat(str(date.today()))
        if (today_date.year - dob.year) < 18:
            time.sleep(1.0)
            print('Too young ')
            time.sleep(1.0)
            quit('Closing... ')
        return dob
    except ValueError:
        print('Invalid date of birth')
        return date_of_birth_check()