import unittest
from password import user

class Testuser(unittest.TestCase):
    def setUp(self):
        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_user.user_name, "Beth")

            self.assertEqual(self.new_user.password, "0780")
        def test_save_user(self):
            '''
            test_save_user test case to test if the user object is saved into the user list
            '''
            self.new_user.save_user() #saving the new contact
            self.assertEqual(len(user.user_list),1)
        def test_delete_user(self):
            ''' 
            test_delete_contact to test if we can remove our contact from our contact list
            '''
            self.new_contact.save_contact()
            test_user = user("test", "user","071234567","beth@user.com")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(user.user_list),1)

        if __name__ == '__main__':
                  unittest.main()              