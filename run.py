import random
import maskpass
from user import User
from credentials import Credentials


def new_user(fname, lname, username, email, password):
  '''function that creates a new user from the user class'''
  
  new_user = User(fname, lname, username, email, password)
  
  return new_user

def save_user(user):
  '''function that saves a new user from the save_user method'''
  User.save_user(user)