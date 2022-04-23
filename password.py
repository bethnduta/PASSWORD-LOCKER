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

    def delete    

