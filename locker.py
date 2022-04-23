import string 
from random import*
from password import User
from password import Credentials
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_user():
    return User.display_users()
def create_account(accountusername,accountname,accountpassword):
    newaccount= Credentials(accountusername, accountname,accountpassword)
    return newaccount
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account()
def find_account(number):
    return Credentials.find_by_number(number)
def display_accounts():
    return Credentials.display_accounts()
def main():
    while True:
        print("welcome: enter PY or BN to start")
        print("PY -or- BN")
        option =input()
        if option == "PY":
            print("create an account")
            print("-"*10)
            print("enter first name...")
            print(f"Name:{firstname}{lastname} \nUsername: {username}\nPassword: {userpassword}")
            print("\nUse Login to your account with your details")
            print("\n \n")

        elif option == "BN":
            print("username...")
            loInUsername=input()
            print("password...")



