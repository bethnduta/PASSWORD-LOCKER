import unittest
from password import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        set up method to run before each testcase
        """
        self.new_user = User("BETH", "Nduta", "0712345678", "beth@gmail.com")  # create user object

    def test_init(self):
        """

            test_init test case to test if the object is initialized properly
            """
        self.assertEqual(self.new_user.firstname, "BETH")
        self.assertEqual(self.new_user.lastname, "Nduta")
        self.assertEqual(self.new_user.username, "0712345678")
        self.assertEqual(self.new_user.password, "beth@gmail.com")

    def test_save_user(self):
        """
            test_save_user test case to test if the user object is saved into the user list
            """
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.usersList), 2)

    def test_delete_user(self):
        """
            test_delete_contact to test if we can remove our contact from our contact list
            """
        self.new_user.save_user()
        test_user = User("BETH", "nduta", "071234567", "beth@gmail.com")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.usersList), 1)


if __name__ == '__main__':
    unittest.main()