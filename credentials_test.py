import unittest #import unittest module

from credentials import Credentials



class test_credentials (unittest.TestCase):
    def setUp(self):
        self.new_credentials_list = Credentials("instagram","Barry_Barack3","9000")
        
    def test_init(self):
      self.assertEqual(self.new_credentials_list.social_site,"instagram")
      self.assertEqual(self.new_credentials_list.username,"Barry_Barack3")
      self.assertEqual(self.new_credentials_list.password,"9000")
      
    def test_save_credentials(self):
        
    
if __name__ == "__main__":
    unittest.main()

    
        