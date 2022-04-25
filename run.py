import random, string
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
  
def new_credentials(site, username, email, password):
  '''function that creates new credentials from the credentials class'''
  
  new_credentials = Credentials(site, username, email, password)
  return new_credentials

def save_credentials(credentials):
  '''function that saves new credentials from the save_credentials method'''
  
  return Credentials.save_credentials(credentials)
  

def display_vault():
  '''function that displays all credentials from the vault method'''
  
  return Credentials.vault()




