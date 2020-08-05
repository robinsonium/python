class BankAccount:
    def __init__(self, int_rate, balance,account_name):
        self.int_rate=int_rate
        self.balance=balance  
    def deposit(self, amount):
        self.balance+=amount
        return(self)
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient funds: charging a $5 fee")
            self.balance-=5
        return(self)
    def display_account_info(self):
	    print("Balance: ",self.balance)
    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance*self.int_rate
        return(self)

# acct1=BankAccount(1.05,400 )
# acct2=BankAccount(1.045,0)
# # acct1.deposit(10).withdraw(5).display_account_info()
# # print(acct1.balance)

# acct1.deposit(75).deposit(50).deposit(100).withdraw(125).yield_interest().display_account_info()
# acct2.deposit(500).deposit(200).withdraw(50).withdraw(20).withdraw(100).withdraw(75).yield_interest().display_account_info()
