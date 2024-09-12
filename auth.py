import json
from user import User
from account import Account



class Auth:
    def __init__(self):
        pass

    def load_users_from_file(self):

        with open('db.json', 'r') as file:

            return json.load(file)['users']


    def authenticate_user(self,users, user_name, password):

        for user in users:

            if user['name'] == user_name and user['password'] == password:

                return user

        return None


    def create_user_object(self,user):

        accounts = {}

        for account in user['accounts']:

            accounts[account['account_number']] = Account(account['balance'])

        return User(user['name'], accounts)


    def login(self, user_name, password):

        users = self.load_users_from_file()

        user = self.authenticate_user(users, user_name, password)

        if user:

            return self.create_user_object(user)

        else:

            return None