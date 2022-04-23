import random
from password import user

def main():
    while True:
        print("welcome")
        print('\n')
        print("select a short code to navigate through: to create new user use 'nu' To login to your account 'lg' or 'ex' to exit")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('create username')
            created_user_name = input()

            print('create password')
            created_user_password = input()

            print('confirm password')
            confirm_password = input()