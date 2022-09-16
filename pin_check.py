import hashlib

# Separatin g the pin check for ease of access
def pin_check():
    raw_pin = (input('Enter your FOUR digit PIN: '))
    if raw_pin.isnumeric() == True and len(raw_pin) == 4:
        raw_pin = int(raw_pin)
    # Hashing the pin for enhanced security
        pin_hash = str(raw_pin)
        encoded=pin_hash.encode()
        pin = hashlib.sha256(encoded).hexdigest()
    else:
        print('Invalid !!\nMust be four digits only!!'.upper())
        return pin_check()
    return pin