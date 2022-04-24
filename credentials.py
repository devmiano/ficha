from user import User
import random

'''class that creates new credentials for a user'''
class Credentials:
  
  
  '''initialize new credentials array'''
  credentials = []
  
  
  '''init method that defines properties for a new credentials object'''
  def __init__(self, site, username, email, password):
    '''arguments for the credentials object'''
    
    self.site = site
    self.username = username
    self.email = email
    self.password = password
    
  