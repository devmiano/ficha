#!/usr/bin/env python3.8

import random, string
import maskpass
from user import User
from credentials import Credentials


def create_user(fname, lname, username, email, password):
  '''function that creates a new user from the user class'''
  
  new_user = User(fname, lname, username, email, password)
  
  return new_user

def save_user(user):
  '''function that saves a new user from the save_user method'''
  User.save_user(user)
  
def remove_user(user):
  '''Remove a user'''
  
  User.remove_new_user(user)
  
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


def createpwd(length, char=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
  '''function that hides and generates a password'''
  
  password = ''.join(random.choice(char) for _ in range(length))
  
  return password


def main():
  print("\n\n================== Ficha Password Manager ====================")
  print('To get started please choose one of the following options from the menu below')
  
  while True: 
    print('Main Menu: \n a - Create new Ficha account \n b - Log into your Ficha account \n x - Close Application \n')
    
    short_code = input("Enter option: ").lower()
    
    if short_code == 'a':
      print('Enter first name:')
      fname = input().strip()
      print('Enter last name:')
      lname = input().strip()
      print('Enter username:')
      username = input().strip()
      print('Enter email:')
      email = input().strip()
      
      print('Create your master password:')
      password = maskpass.askpass(mask='*')
      
      save_user(create_user(fname, lname, username, email, password))
      
      print('\n')
      
      print(f'Welcome {fname} {lname}')
      
      print('\n')
      
      print(f'Username: {username} Email: {email} Password: {password}')
      
      print('App Menu: \n c - Create new Credentials \n d - Log out of Ficha account')
      
    elif short_code == 'x':
      print('Thank you for choosing Ficha Password Manager! See you later!')
      break
        
    else:
      print('\n')
      print('Wrong option! Please choose the right one')
      
if __name__ == '__main__':
  main()
  