import string
from random import * 
from password import User
from locker import Credentials 
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def find_user(number):
    return User.find_by_number(number)
def display_users():
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
        print("welcome to Password Locker App: enter PY(to create account) or BN(to login) to start")
        print("PY -or- BN")
        option =input()
        if option == "PY":
            print("create an account")
            print("-"*10)
            print("enter first name...")
            firstname = input()
            print("enter last name")
            lastname = input()
            print("create username")
            username=input()
            print("create password")
            userpassword=input()
            save_user(create_user(firstname,lastname,username,userpassword))
            print("account createdv successfully. your details:")
            print("_"*10)
            print(f"Name: {firstname} {lastname} \nUsername: {username} \nPassword: {userpassword}")
            print("\nUse Login to your account with your details")
            print("\n \n")

        elif option == "BN":
            print("username...")
            logInUsername=input()
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
                    print(f"password: {accountpassword}")
                elif decision == "N":
                    print("enter your password")
                    accountpassword=input()
                else:
                    print("put in a valid choice")
                    save_account(create_account(accountusername, accountname, accountpassword))
                    print("\n")
                    print(f"username:{accountusername} \nAccount Name: {accountname}\npassword: {accountpassword}")
            elif choose == "TC":
                    if find_account(accountusername):
                        print("your credential accounts:")
                        print("_"*25)
                        for user in display_accounts():
                            print(f"account: {user.accountname}\npassword:{user.accountpassword}\n\n")
                        else:
                            print("incorrect credentials")
            else:
                            print("TRY Again")
                            print("\n")
        else:
                                print("incorrect information")
                                print("\n")
                                
    else:
        print("choose a valid option")
                                    
        print("\n")

if __name__ == '__main__':
    main()     
           
                       


