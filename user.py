class User:
  '''class that generates a new user'''
  pass

  '''initialize new users array'''
  users = []
  
  '''an init method that defines properties for a new user object'''
  def __init__(self, fname, lname, username, email, password):
    '''arguments for the user object'''
    
    self.fname = fname
    self.lname = lname
    self.username = username
    self.email = email
    self.password = password
    
  '''method to save users in the users array'''
  def save_user(self):
    User.users.append(self)
    
  '''method to delete users in the users array'''
  def delete_user(self):
    User.users.remove(self)
    
  
  '''class method to retrieve a user in the users array for sign in'''
  @classmethod
  def get_user(cls, username, password):
    for user in cls.users:
      if user.username == username and user.password == password:
        return True
