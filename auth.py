import json
from user import User
from account import Account
from message import Message

message = Message()

class Auth:
    def __init__(self):
        pass

    def login(self, user_name, password):
        with open('db.json', 'r') as file:
            users = json.load(file)['users']

        for user in users:
            if user['name'] == user_name:
                if user['password'] == password:
                    accounts = {}
                    for account in user['accounts']:
                        accounts[account['account_number']] = Account(account['balance'])
                    return User(user['name'], accounts)
                else:
                    print("name or password not found")
            else:
                print("name or password not found")
            
        return None
