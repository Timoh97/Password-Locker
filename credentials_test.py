import unittest #import unittest module

from credentials import Credentials



class test_credentials (unittest.TestCase):
    def setUp(self):
        self.new_credentials_list = Credentials("instagram","Barry_Barack3","9000")
        
    def tearDown(self):
        Credentials.credentials_list = []
        
        
    def test_init(self):
      self.assertEqual(self.new_credentials_list.social_site,"instagram")
      self.assertEqual(self.new_credentials_list.username,"Barry_Barack3")
      self.assertEqual(self.new_credentials_list.password,"9000")
      
    def test_save_credentials(self):
        self.new_credentials_list.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
        
    def test_delete(self):
        self.new_credentials_list.save_credentials()
        test_usercredentials = Credentials("Facebook","James white","0000")
        test_usercredentials.save_credentials()
        self.new_credentials_list.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
        
        
    # def test_display_credentials(self):
    #     self.new_credentials_list()
    #     self.assertEqual(len(Credentials.credentials_list),1)
        
        
    
if __name__ == "__main__":
    unittest.main()

    
        