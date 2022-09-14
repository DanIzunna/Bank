class Savings_Account():
    def __str__(self):
        return 'Savings Account'
    def deposit():
        deposit_amt = float(input('Enter a deposit amount NGN N: '))
        if deposit_amt < 10000:
            print('Deposit too low!!')
            return Savings_Account.deposit()
        else:
            print('Successfully deposited N%s into the account'%deposit_amt)
        return deposit_amt
# Savings_Account.deposit()