import unittest
from password import User

class Testuser(unittest.TestCase):
    def setUp(self):
        '''
        set up method to run before each testcase
        '''
        self.new_user = User("James","Muriuki","0712345678","james@ms.com") # create user object

        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_user.first_name,"Beth")
            self.assertEqual(self.new_user.last_name,"Nduta")
            self.assertEqual(self.new_user.phone_number,"0712345678")
            self.assertEqual(self.new_user.email,"beth@gmail.com")
        def test_save_user(self):
            '''
            test_save_user test case to test if the user object is saved into the user list
            '''
            self.new_user.save_user() #saving the new user
            self.assertEqual(len(User.user_list),1)
        def test_delete_user(self):
            ''' 
            test_delete_contact to test if we can remove our contact from our contact list
            '''
            self.new_User.save_User()
            test_user = User("test", "Beth","nduta","071234567","beth@user.com")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)

        if __name__ == '__main__':
                  unittest.main()              