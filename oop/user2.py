from bank_account import BankAccount

class User:
    def __init__(self,username,email_address):
        self.name=username
        self.email=email_address
        self.account=[]
    def create_account(self,int_rate,balance,account_name):
        self.account.append(BankAccount(int_rate,balance,account_name))
        return(self)
    def make_deposit(self,amount,account_name):
        if  len(self.account.account_name)==0:
            print(f"Error, {self.name} has no account created")
        else:
            self.account.account_name.balance+=amount
            return(self)
    def make_withdrawal(self,amount):
        if not self.account:
            print(f"Error, {self.name} has no account created")
        else:
            self.account.balance-=amount
            return(self)
    def display_user_balance(self):
        if not self.account:
            print(f"Error, {self.name} has no account created")
        else:
            print(self.account,":",self.account.balance)
    def transfer_money(self,other_user,amount):
        other_user.make_deposit(amount)
        self.account.balance-=amount
        return(self)

brian=User("brian","brian@dojo.com")
jess=User("Jessica","Jess@dojo.com")
rae=User("Raelynn","rae@dojo.com")
# brian.create_account(1.04,200,"checking")

brian.make_deposit(150).make_deposit(200).make_deposit(50).make_withdrawal(200).display_user_balance()
# jess.make_deposit(75).make_deposit(425).make_deposit(50).make_withdrawal(50).display_user_balance()
# rae.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
# brian.transfer_money(rae,150).display_user_balance()
# brian.account.yield_interest().display_account_info()
# rae.display_user_balance()

 