from user import User



class Credentials:
  '''class that creates new credentials for a user'''
  
  credentials = []
  '''initialize the credentials array'''
  
  def __init__(self, site, username, email, password):
    '''init method that defines properties for a new credentials object'''
    
    self.site = site
    self.username = username
    self.email = email
    self.password = password
    '''arguments for the credentials object'''

        
  def save_credentials(self):
    '''method to save credentials in the credentials array'''
    Credentials.credentials.append(self)
  
  
        
  def delete_credentials(self):
    '''method to delete credentials in the credentials array'''
    Credentials.credentials.remove(self)
  
  
  
  @classmethod  
  def vault(cls):
    '''class method to display all credentials in the vault'''

    return cls.credentials
  