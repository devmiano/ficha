from user import User



'''class that creates new credentials for a user'''
class Credentials:
  
  
  '''initialize the credentials array'''
  credentials = []
  
  
  '''init method that defines properties for a new credentials object'''
  def __init__(self, site, username, email, password):
    '''arguments for the credentials object'''
    
    self.site = site
    self.username = username
    self.email = email
    self.password = password

  '''method to save credentials in the credentials array'''      
  def save_credentials(self):
    Credentials.credentials.append(self)
  
  
  '''method to delete credentials in the credentials array'''      
  def delete_credentials(self):
    Credentials.credentials.remove(self)
  
  
  '''class method to display all credentials in the vault'''
  @classmethod  
  def vault(cls, username, password):
    vault_admin = User.get_user(username, password)
    
    if vault_admin == username:
      return cls.credentials
    