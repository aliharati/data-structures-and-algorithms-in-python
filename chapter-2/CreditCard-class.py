class CreditCard:

    """A consumer credit card"""

    def __init__(self,customer, bank, acnt, limit, balance=0): # R-2.7
        """Creates a new credit card instance
        
        The initial balance is zero
        
        customer  the name of the customer (e.g., 'John Goodman')
        bank      the name of the bank (e.g., 'California Saving')
        acnt      the acount identifier (e.g, '5491 0375 0934 9320')
        limit     creat limit (mesured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance


    def get_customer(self):
        """Return name of the customer"""
        return self._customer
        
    def get_bank(self):
        """Return the name of the bank"""
        return self._bank
        
    def get_acnt(self):
        """Return the account identifier"""
        return self._acnt
        
    def get_limit(self):
        """Return the account limit"""
        return self._limit
        
    def get_balance(self):
        """Return the account balance"""
        return self._balance
        
    def charge(self, price): # R-2.5
        """Charge given price to the card, assuming sufficient credit limit
            
        Return True if charge was processed. False if charge was denied.
        """
        if not isinstance(price, (int,float)):
            raise TypeError('The charged price must be numeric')
        if price + self._balance > self._limit:
            return False
        self._balance += price
        return True
        
    def make_payment(self,amount): # R-2.5 & R-2.6
        """Process customer payment that reduces balance."""
        if not isinstance(amount, (int,float)):
            raise TypeError('The given amount must be numeric')
        elif amount < 0:
            raise ValueError('The given amount must be positive')
        self._balance -= amount
    

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard( 'John Bowman' , 'California Savings' ,
                             '5391 0375 9387 5309' , 2500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Federal' , 
                             '3485 0399 3395 1954' , 3500) )
    wallet.append(CreditCard( 'John Bowman' , 'California Finance' , 
                             '5391 0375 9387 5309' , 5000) )
    for val in range(1,120):
        
        if wallet[0].charge(val) is True:
            wallet[0].charge(val)
        else:
            print('wallet 0 is out')
        if wallet[1].charge(2*val) is True:
            wallet[1].charge(2*val)
        else:
            print('wallet 1 is out')
        if wallet[2].charge(3*val) is True:
            wallet[2].charge(3*val)
        else:
            print('wallet 2 is out')
    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_acnt())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        # while wallet[c].get_balance() > 100:
        #     wallet[c].make_payment(100)
        #     print("New balance =", wallet[c].get_balance())
        print()