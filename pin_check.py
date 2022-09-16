import hashlib

# Separating the pin check for ease of access
def pin_check():
    raw_pin = (input('Enter your FOUR digit PIN: '))
    if raw_pin.isnumeric() == True and len(raw_pin) == 4:
        raw_pin = int(raw_pin)

    # Hashing the pin for enhanced security
        pin_hash = str(raw_pin)
        encoded=pin_hash.encode()
        pin = hashlib.sha256(encoded).hexdigest()

    elif raw_pin.isnumeric() != True:
        print('Invalid !!\npin Must be numbers only!!'.upper())
        return pin_check()

    elif raw_pin.isnumeric() == True and len(raw_pin) > 4:
        print('Invalid !!\npin Must be four digits only!!'.upper())
        return pin_check()
    return pin