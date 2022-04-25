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
    
  