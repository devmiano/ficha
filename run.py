#!/usr/bin/env python3.8

import random, string
import maskpass
import pyperclip
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
  
def new_credentials(site, site_username, site_email, site_password):
  '''function that creates new credentials from the credentials class'''
  
  new_credentials = Credentials(site, site_username, site_email, site_password)
  return new_credentials

def save_credentials(credentials):
  '''function that saves new credentials from the save_credentials method'''
  
  return Credentials.save_credentials(credentials)
  

def display_vault():
  '''function that displays all credentials from the vault method'''
  
  return Credentials.vault()


def createpwd(length, char=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
  '''function that hides and generates a password'''
  
  password = ''.join(random.choice(char) for _ in range(int(length)))
  
  return password


def main():
  print("\n\n================== Ficha Password Manager ====================\n")
  print('To get started please choose one of the following options from the menu below \n')
  
  while True: 
    print('Main Menu: \n a - Create new Ficha account \n b - Log into your Ficha account \n x - Close Application \n')
    
    short_code = input("Enter option: ").lower()
    
    if short_code == 'a':
      fname = input('Enter first name: ').strip()
      lname = input('Enter last name: ').strip()
      username = input('Enter username: ').strip()
      email = input('Enter email: ').strip()
      print('\n')
      password = maskpass.askpass(prompt="Create your master Password: ", mask='*')
      
      save_user(create_user(fname, lname, username, email, password))
      
      print('\n')
      print('Please now log in to start generating and saving your passwords')
      print('\n')
      
    elif short_code == 'b':
      print("\n\n================== Log in ====================\n")
      username = input('Enter username: ').strip()
      password = maskpass.askpass(prompt="Enter your master Password: ", mask='*')
      
      username = User.get_user(username, password)
      
      if username == username:
        print('\nLogin successful!')
        print(f"\n================== {fname.capitalize()} {lname.capitalize()}'s Vault ====================\n")
        print(f'Welcome to Ficha Password Manager {username}')
        
        while True:
          print('\n')
          
          print('App Menu: \n c - Create new Credentials \n d - View your Vault \n e - Copy Credentials \n f - Log out \n ')
          
          short_code = input("Enter option: ").lower()
          
          print('\n')
          if short_code == 'c':
            print('Create new Credentials')
            print('\n')
            site = input('Enter site name: ').strip()
            site_username = input('Enter site username: ').strip()
            site_email = input('Enter site email: ').strip()
            
            while True:
              print('\n')
        
              print('Enter "m" to create your password manually \nEnter "n" to generate a password.')
              short_code = input("Enter option: ").lower()
              
              if short_code == 'y':
                site_password = maskpass.askpass(prompt="Enter your site Password: ", mask='*')
                break
              elif short_code == 'n':
                print()
                length = input('Enter a password length: ').strip()
                site_password = createpwd(length)
                break
              else:
                print('No option specified')
                break
            
            save_credentials(new_credentials(site, site_username, site_email, site_password))
            print('\n')
            
            print(f'Successfully created new credentials for {username} \n Site name: {site}\n Username: {site_username} \n Email: {site_email} \n Password: {site_password}')
            
            
            
          elif short_code == 'd':
            print(' ')
            if Credentials.find_vault(username, password):
              print('\n')
              for credentials in display_vault():
                print(f' Credentials for {credentials.site.capitalize()}')
                print(f' Site username: {credentials.site_username}')
                print(f' Site email: {credentials.site_email}')
                print(f' Site password: {credentials.site_password}')
                print('\n')
                
            else:
              print(f'\nNo credentials found. Please try creating new credentials first')
              
          elif short_code == 'e':
            while True:
              print('\n')
              print('Enter "m" to copy your your credentials or "n" to exit')
              short_code = input("Enter option: ").lower()
                
              if short_code == 'm':
                print('\nFilter credentials by site name\n')
                copy_credentials = input("Enter site name: ").strip()
                
                for credentials in display_vault():
                  if credentials.site == copy_credentials:
                    pyperclip.copy(f'{credentials.site_username} {credentials.site_password}')
                    print(f'\nCopied {credentials.site} to clipboard')
                    break
                    
                  else:
                    print('No credentials found')
                    break
                
              elif short_code == 'n':
                print('Exited successfully!')
                break
              else:
                print('\nNo option specified')
                break
              
          elif short_code == 'f':
            print('Are you sure you want to proceed? \nEnter "y" to logout \nEnter "n" to cancel')
            short_code = input("Enter option: ").lower()
            
            if short_code == 'y':
                print('\nLogged out successfully')
                break
            elif short_code == 'n':
              print('\nProcess cancelled')
            else:
              print('\nNo option specified')
              
          else:
            print('\nNo option specified please try again and select from the list')
           
      else:    
        print("\n You do not have an account with us please create one to continue \n") 
      
    elif short_code == 'x':
      print('Thank you for choosing Ficha Password Manager! See you later!')
      break
        
    else:
      print('\n')
      print('Wrong option! Please choose the right one')
      
if __name__ == '__main__':
  main()
  