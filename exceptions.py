class BankingExcpetion(Exception):
    pass

class InsufficientFundsException(BankingExcpetion):
    def message(self):
        return 'An error occurred: Insufficent Funds'

class InvalidAccountNumberException(BankingExcpetion):
    def message(self):
        return "An error occurred: Invalid Account Number"