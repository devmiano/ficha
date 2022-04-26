class User:
  '''class that generates a new user'''
  pass

  
  users = []
  '''initialize new users array'''
  
  def __init__(self, fname, lname, username, email, password):
    '''an init method that defines properties for a new user object'''
    
    
    self.fname = fname
    self.lname = lname
    self.username = username
    self.email = email
    self.password = password
    '''arguments for the user object'''
    
  
  def save_user(self):
    '''method to save users in the users array'''
    User.users.append(self)
    
  
  def delete_user(self):
    '''method to delete users in the users array'''
    User.users.remove(self)
    
  
  
  @classmethod
  def get_user(cls, username, password):
    '''class method to retrieve a user in the users array for sign in'''
    for user in cls.users:
      if user.username == username and user.password == password:
        current_user = user.username
        return current_user
      
  
  
  @classmethod
  def display_all_users(cls):
    '''class method to retrieve a user in the users array for display'''
    return cls.users


