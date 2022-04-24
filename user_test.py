import unittest
from user import User


'''class that defines test cases for the user class'''
class TestUser(unittest.TestCase):
  
  
  '''method to run before the test case is executed'''
  def setUp(self):
    self.new_user = User('Annabel', 'Karish', 'annabelkarish', 'annabel@karish.com', 'Karish@Annabel2022')
  
  
  '''method to test that the object is initialized'''
  def test_init(self):
    self.assertEqual(self.new_user.f_name, 'Annabel')
    self.assertEqual(self.new_user.l_name, 'Karish')
    self.assertEqual(self.new_user.username, 'annabelkarish')
    self.assertEqual(self.new_user.email, 'annabel@karish.com')
    self.assertEqual(self.new_user.password, 'Karish@Annabel2022')
  
  
  '''method to test run after the test case is executed'''  
  def tearDown(self):
    User.users = []
    
  '''method to test that the user is saved'''
  def test_save_user(self):
    self.new_user.save_user()
    self.assertEqual(len(User.users), 1)
    
  '''method to test that multiple users can be saved'''
  def test_save_new_users(self):
    self.new_user.save_user()
    test_user = User('First', 'User', 'first@user.com', 'firstuser', 'first@user2022')
    test_user.save_user()
    self.assertEqual(len(User.users), 2)
    