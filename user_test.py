import unittest
from user import User



class TestUser(unittest.TestCase):
  '''class that defines test cases for the user class'''
  
  
  def setUp(self):
    '''method to test the creation of a new user object'''
    self.new_user = User('Annabel', 'Karish', 'annabelkarish', 'annabel@karish.com', 'Karish@Annabel2022')
  
    
  
  def test_init(self):
    self.assertEqual(self.new_user.fname, 'Annabel')
    self.assertEqual(self.new_user.lname, 'Karish')
    self.assertEqual(self.new_user.username, 'annabelkarish')
    self.assertEqual(self.new_user.email, 'annabel@karish.com')
    self.assertEqual(self.new_user.password, 'Karish@Annabel2022')
    '''method to test that the object is initialized'''
  
  
  
  def tearDown(self):
    '''method to test run after the test case is executed'''  
    User.users = []
    
  
  def test_save_user(self):
    '''method to test that the user is saved'''
    self.new_user.save_user()
    self.assertEqual(len(User.users), 1)
    
  
  def test_save_new_users(self):
    '''method to test that multiple users can be saved'''
    self.new_user.save_user()
    test_user = User('First', 'User', 'first@user.com', 'firstuser', 'first@user2022')
    test_user.save_user()
    self.assertEqual(len(User.users), 2)
    
  def test_delete_user(self):
    '''method to test that a user can be deleted''' 
    self.new_user.delete_user()
    self.assertEqual(len(User.users), 0)
    
  
  def test_display_all_users(self):
    '''method to test that all users can be displayed''' 
    self.assertEqual(User.display_all_users(), User.users)
    
if __name__ == '__main__':
  unittest.main()