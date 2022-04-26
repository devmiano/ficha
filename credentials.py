from user import User



class Credentials:
  '''class that creates new credentials for a user'''
  
  credentials = []
  '''initialize the credentials array'''
  
  def __init__(self, site, site_username, site_email, site_password):
    '''init method that defines properties for a new credentials object'''
    
    self.site = site
    self.site_username = site_username
    self.site_email = site_email
    self.site_password = site_password
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
  
  @classmethod  
  def find_vault(cls, username, password):
    '''class method to display all credentials in the vault'''
    find = ''
    for user in User.users:
      if user.username == username and user.password == password:
        find = user.username
    return find
  
  