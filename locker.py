import string 
from random import*
from password import User
from password import credentials 
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
    newaccount= credentials(accountusername, accountname,accountpassword)
    return newaccount
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account()
def find_account(number):
    return credentials.find_by_number(number)
def display_accounts():
    return credentials.display_accounts()
def main():
    while True:
        print("welcome: enter PY or BN to start")
        print("PY -or- BN")
        option =input()
        if option == "PY":
            print("create an account")
            print("-"*10)
            print("enter first name...")
            # print(f"Name:{firstname}{lastname} \nUsername: {username}\nPassword: {userpassword}")
            print("\nUse Login to your account with your details")
            print("\n \n")

        elif option == "BN":
            print("username...")
            loInUsername=input()
            print("password...")
            logInPassword=input()
            if find_user(logInPassword):
                print("\n")
                print("you can create multiple account (MC) and also view them (TC)")
                print("_"*60)
                print("MC -or- TC")
                choose = input()
                print("\n")
            if choose == "MC":
                print("add credential account")
                print("_"*25) 
                accountusername=logInUsername   
                print("Account Name")
                accountname = input()
                print("\n")
                print("generate automatic password (G) OR CREATe new password (N)")
                decision=input()
                if decision == "G":
                    characters=string.ascli_letters + string.digits
                    accountpassword = "", join(choice(characters)for x in range(randint(6,16)))
                    print(f"password: {accountpassword")
                elif decision == "N":
                    print("enter your password")
                    accountpassword=input()
                else:
                    print("put in a valid choice")
                    save_account(create_account(accountusername, accountname, accountpassword))
                        

                       


