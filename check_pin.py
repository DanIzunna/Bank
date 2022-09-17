import hashlib
import time

def pin_check():
    _pin = (input('Create your FOUR digit secret PIN: '))
    if _pin.isnumeric() == True and len(_pin) == 4:
        _pin = int(_pin)
        
        raw_pin = input('Confirm your PIN: ')
        if raw_pin.isnumeric() == True and len(raw_pin) == 4:
            raw_pin = int(raw_pin)
        if raw_pin == (_pin):
        # Hashing the pin for enhanced security
            pin_hash = str(raw_pin)
            encoded=pin_hash.encode()
            pin = hashlib.sha256(encoded).hexdigest()
            return pin
        elif raw_pin != _pin:
            print('Passwords don\'t match!')
            return pin_check()

    elif _pin.isnumeric() != True:
        print('Invalid !!\npin Must be numbers only!!'.upper())
        return pin_check()

    elif _pin.isnumeric() == True and len(_pin) > 4:
        print('Invalid !!\npin Must be four digits only!!'.upper())
        return pin_check()