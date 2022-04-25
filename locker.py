import random
import string

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
                            '''
                            method that returns a list of the accounts
                            '''
                            for account in cls.accounts:
                                return cls.accounts
                        @classmethod
                        def find_by_number(cls,number):
                            '''
                            method that takes in a number and returns a contact that matches that number
                            '''
                            for account in cls.accounts:
                                if account.accountusername == number:
                                    return account        
