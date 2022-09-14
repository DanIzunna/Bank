class Fixed_Deposit_Account():
    def __str__(self):
        return 'Fixed Deposit Account'


    def deposit():
        deposit_amt = float(input('Enter a deposit amount NGN N: '))
        if deposit_amt < 10000:
            print('Deposit too low!!')
            return Fixed_Deposit_Account.deposit()
        else:
            for month in range(1, 12, 4):
                print('\t %s Months'%month)#, '\t %s Years'%month)
            # duration = int(input('Enter the duration of the deposit'))
            # interest_rate =  
            # To make interrest rate dynamically generated based on the amount deposited and the duration
            print('Successfully deposited N%s into the account'%deposit_amt)
        return deposit_amt

# Fixed_Deposit_Account.deposit()