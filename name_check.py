import time

def first_name_check():
    first_name = input('Please Enter your First Name: ')
    time.sleep(0.5)
    if first_name.isalpha() == True:
        first_name = first_name.upper()
    else:
        print('Invalid Name!!')
        return first_name_check()
    return first_name

def last_name_check():
    last_name = input('Please Enter your  Last Name: ')
    if last_name.isalpha() == True:
        last_name = last_name.upper()
    else:
        print('Invalid Name!!')
        return last_name_check()
    return last_name