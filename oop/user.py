class User:
    def __init__(self,username,email_address):
        self.name=username
        self.email=email_address
        self.account_balance=0
    def make_deposit(self,amount):
        self.account_balance+=amount
        return(self)
    def make_withdrawal(self,amount):
        self.account_balance-=amount
        return(self)
    def display_user_balance(self):
        print(self.name,":",self.account_balance)
    def transfer_money(self,other_user,amount):
        other_user.make_deposit(amount)
        self.account_balance-=amount
        return(self)


brian=User("brian","brian@dojo.com")
jess=User("Jessica","Jess@dojo.com")
rae=User("Raelynn","rae@dojo.com")
# brian.make_deposit(150)
# brian.make_deposit(200)
# brian.make_deposit(50)
# brian.make_withdrawal(200)
# brian.display_user_balance()
# jess.make_deposit(75)
# jess.make_deposit(425)
# jess.make_withdrawal(50)
# jess.make_withdrawal(50)
# jess.display_user_balance()
# rae.make_deposit(100)
# rae.make_deposit(200)
# rae.make_deposit(300)
# rae.make_withdrawal(50)
# rae.display_user_balance()
# brian.transfer_money(rae,150)
brian.make_deposit(150).make_deposit(200).make_deposit(50).make_withdrawal(200).display_user_balance()
jess.make_deposit(75).make_deposit(425).make_deposit(50).make_withdrawal(50).display_user_balance()
rae.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
brian.transfer_money(rae,150).display_user_balance()
# brian.display_user_balance()
rae.display_user_balance()

 