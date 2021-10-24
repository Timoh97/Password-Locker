import unittest  #import unittest module
from user import User #import user to make it accessible for testing


class test_user (unittest.TestCase):

    def setUp(self):
        self.new_user = User("Timothy", "Mugendi", "987900")

    def tearDown(self):
        User.list_user = []

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Timothy")
        self.assertEqual(self.new_user.last_name, "Mugendi")
        self.assertEqual(self.new_user.password, "987900")

    def test_save(self):
        self.new_user.save_details()
        self.assertEqual(len(User.list_user), 1)

    def test_delete(self):
        self.new_user.save_details()
        test_user = User("Kelvin", "Kimani", "00000")
        test_user.save_details()
        self.new_user.delete_details()
        self.assertEqual(len(User.list_user), 1)

    def test_multipleUser_saves(self):
        self.new_user.save_details()
        test_user = User("Kelvin", "Kimani", "00000")
        test_user.save_details()
        self.assertEqual(len(User.list_user), 2)

    def search_byUsername(self):
        self.new_user.save_details()
        test_user = User("Kelvin", "Kimani", "00000")
        test_user.save_details()
        searched_user = User.search_byFirstName("Kelvin")
        self.assertEqual(searched_user.last_name, test_user.last_name)


if __name__ == "__main__":
    unittest.main()
