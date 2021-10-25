import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Timothy', '9000T')

    def test_init(self):
        self.assertEqual(self.new_user.username, 'Timothy')
        self.assertEqual(self.new_user.password, '9000T')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)