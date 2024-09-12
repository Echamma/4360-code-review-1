from message import Message
from exceptions import BankingExcpetion, Invalidaccount_numberException


message = Message()

class User:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    def show_accounts(self):
        message.print("{:<20}{:<0}".format("Account Number", "Amount"))
        for key,val in self.accounts.items():
            balance = val.check_balance()
            message.print("{:<20}{:<0}".format(key, balance))

    
    def deposit(self, args):
        try:
            account_number = int(args[0])
            amount = int(args[1])
            account = self.accounts.get(account_number)
            
            if not account:
                raise Invalidaccount_numberException

            account.deposit(amount)
            return account.check_balance()
        except BankingExcpetion as e:
            message.print(e.message())
        except:
            message.print("An error occurred")

    def withdraw(self, args):
        try:
            account_number = int(args[0])
            amount = int(args[1])
            account = self.accounts[account_number]

            if not account:
                raise Invalidaccount_numberException

            account.withdraw(amount)
            return account.check_balance()
        except BankingExcpetion as e:
            message.print(e.message())
        except:
            message.print("An error occurred")


    def transfer(self, args):
        from_account_number = int(args[0])
        to_account_number = int(args[1])
        amount = int(args[2])

        account1 = self.accounts[from_account_number]
        account2 = self.accounts[to_account_number]

        if not account1 or not account2:
            raise Invalidaccount_numberException

        account1.withdraw(amount)
        account2.deposit(amount)