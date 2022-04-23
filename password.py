from collections import UserList
import random
import string

class User:
    '''
    class that generates new instances of users
    '''
    UserList = []
    def __init__(self,firstname,lastname,username,password):
        '''
        __init__method that helps us define properties for our objectself
        '''
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
    def save_user(self):
        '''
        save_user method saves user info into user userslist
        '''
        User.usersList.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the userslist
        '''
        User.UserList.remove(self)
    @classmethod
    def display_users(cls):
        '''
        method that returns info from the userslist
        '''
        return cls.UserList  
    @classmethod
    def find_by_number(cls,number):
        '''
        method that takes in a username and returns a user that matches that number
        '''
        for user in cls.UserList:
            if user.password == number:
                return user
        @classmethod
        def user_exist(cls,number):
            for user in cls.userslist:
                if user.username == number:
                    return True
                    return False
            class Credentials:
                '''
                class that generates new instances of credentials
                '''
                accounts =[]
                def __init__(self, accountusername, accountname,accountpassword):
                        ''' 
                        __init__ method that helps us define prpoerties for our objectself
                        '''
                        self.accountusername = accountusername
                        self.accountname = accountname
                        self.accountpassword = accountpassword
                def save_account(self):
                        '''
                        save_account method saves user info into accounts
                        '''                           
                        Credentials.accounts.append(self)
                        '''
                        save account method saves user info into accounts
                        '''
                    def delete_account(self):
                        '''
                        delete_account method deletes a saved credential from accounts
                        '''
                        Credentials.accounts.remove(self)
                        @classmethod
                        def display_accounts(cls):
                            
