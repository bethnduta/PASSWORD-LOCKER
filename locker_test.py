import unittest
from locker import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        set up method to run before each testcase

        '''
        self.new_user = Credentials("Beth","Nduta","0712345678","beth@gmail.com") # create credentials object
        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_Credentials.Credentials_name, "Beth")

            self.assertEqual(self.new_Credentials.password, "0780")
        def test_save_Credentials(self):
            '''
            test_save_user test case to test if the user object is saved into the user list
            '''
            self.new_Credentials.save_credentials() #saving the new contact
            self.assertEqual(len(Credentials.Credentials_list),1)
        def test_delete_Credentials(self):
            ''' 
            test_delete_contact to test if we can remove our contact from our contact list
            '''
            self.new_credentials.save_contact()
            test_Credentials = Credentials("test", "credentials","071234567","beth@user.com")
            test_Credentials.save_Credentials()

            self.new_Credentials.delete_Credentials()
            self.assertEqual(len(Credentials.Credentials_list),1)

        if __name__ == '__main__':
                  unittest.main()              