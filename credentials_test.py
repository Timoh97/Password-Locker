import  unittest
from  credentials import User, Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Timothy','97800T')
        
    def test_init(self):
        self.assertEqual(self.new_user.username,'Timothy')
        self.assertEqual(self.new_user.password,'97800T')
        
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.new_credentials = Credentials('Twitter','Timothy','97800T')
        
    def  test_init(self):
        self.assertEqual(self.new_credentials.account_name,'Twitter')
        self.assertEqual(self.new_credentials.username,'Timothy')
        self.assertEqual(self.new_credentials.password,'97800T')
        
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        Credentials.credentials_list = []
        
    def test_save_multiple_accounts(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Timothy','97800T')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def test_delete_credential(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Timothy','97800T')
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Timothy','97800T')
        test_credentials.save_credentials()
        found_credentials = Credentials.find_account_name('Twitter')
        self.assertEqual(found_credentials.account_name,test_credentials.account_name)
        
    def test_credentials_exist(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials('Twitter','Timothy','97800T')
        test_credentials.save_credentials()
        credentials_exist = Credentials.credentials_exist('Twitter')
        self.assertTrue(credentials_exist)
        
    def display_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
        
        
        
if __name__ == '__main__':
    unittest.main()    