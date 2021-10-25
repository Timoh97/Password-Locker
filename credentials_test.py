import unittest
from credentials import Credentials



class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials = Credentials('Twitter', 'Timothy', "9000T")

    def test_init(self):
        self.assertEqual(self.new_credentials.account_name, 'Twitter')
        self.assertEqual(self.new_credentials.username, 'Timothy')
        self.assertEqual(self.new_credentials.password, '9000T')

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_save_multiple_accounts(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter', 'Timothy', '9000T')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter', 'Timothy', '9000T')
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter', 'Timothy', '9000T')
        test_credentials.save_credentials()
        found_credentials = Credentials.find_account_name('Twitter')
        self.assertEqual(found_credentials.account_name,
                         test_credentials.account_name)

    def test_credentials_exist(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter', 'Timothy', '9000T')
        test_credentials.save_credentials()
        credentials_exist = Credentials.credentials_exist('Twitter')
        self.assertTrue(credentials_exist)

    def display_credentials(self):
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()
