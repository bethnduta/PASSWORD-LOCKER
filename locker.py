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

            while confirm_password != created_user_password:
                print("incorrect password")
                print("enter correct password")
                created_user_password = input()
                
                else:
                    
                    print("kudos (created_user_name)! you have successfully created your account")
                    print('\n')
                    print("login")
                    print("username")
                    entered_username = input()
                    print("enter your password")
                    entered_password = input()

                    while entered_username != created_user_name or entered_password !=created_user_password:
                        print("incorrect username or password")
                        print("username")
                        entered_username = input()
                        print("your password")
                        entered_password = input()

                    while entered_username != created_user_name or entered_password != created_user_password:
                        print("incorrect username or password")
                        print("username")
                        entered_username = input()

                        else:
                            print("welcome: (entered_username" to your account)
                            print('\n')
                        elif short_code == 'lg':
                            print("welcome")
                            print("enter user name")
                            default_user_name = input()

                            print("enter password")
                            default_user_password = input()
                            print('\n')
                            while default_user_name != 'testuser' or default_user_password != '09076':
                                print("")
                            
