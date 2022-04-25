import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
  '''class that tests the credentials class'''
  
  def setUp(self):
    '''method to test the creation of a new credentials object'''
    self.new_credentials = Credentials('fb', 'annabelkarish', 'annabel@karish.com', 'annabel')
  
  def __init__(self):
    '''method to test that the object is initialized'''
    
    self.assertEqual(self.new_credentials.site, 'fb')
    self.assertEqual(self.new_credentials.username, 'annabelkarish')
    self.assertEqual(self.new_credentials.email, 'annabel@karish.com')
    self.assertEqual(self.new_credentials.password, 'annabel')
    
    
  def tearDown(self):
    '''method to test run after the test case is executed'''
    Credentials.credentials = []
    
  def test_save_credentials(self):
    '''method to test that the credentials are saved'''
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials), 1)
    
  def test_delete_credentials(self):
    '''method to test that the credentials are deleted'''
    self.new_credentials.delete_credentials()
    self.assertEqual(len(Credentials.credentials), 0)
    
if __name__ == '__main__':
  unittest.main()
  