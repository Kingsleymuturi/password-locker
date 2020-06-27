#!/usr/bin/env python3.7
from app import User, Credentials

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks whether a user exists and then login the user.
    """
  
    return Credentials.verify_user(username,password)

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credentials.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A function that copies the password using the pyperclip framework
    """
    return Credentials.copy_password(account)


def passlocker():
    print('\n')
    print('*'*10 + "PASSWORD LOCKER APP" + '*'*10)
    print('\n')
    while True :
        print("Hello! Welcome to Password Locker App!\n Please type one of the following short codes to proceed.\n NA ---  Create New Account  \n LI ---  Log in to your account  \n EXIT --- Exit application \n")
        short_code=input("").lower().strip()
        if short_code == "na":
            print("Sign Up")
            print('*' * 50)
            username = input("Username: ")
            while True:
                print(" OP - To type your own pasword:\n GP - To generate a random Password for your account")
                password_Choice = input().lower().strip()
                if password_Choice == 'op':
                    password = input("Enter Password\n")
                    save_user(create_new_user(username,password))
                    print("*"*85)
                    print(f"Hello {username}!, Your account has been created succesfully!.")
                    print("Proceed to log in!")
                    print('\n')
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    print("*"*85)
                    print(f"Hello {username}!, Your account has been created succesfully! Your password is: ({password}).")
                    print("Proceed to log in!")
                    print('\n')
                    break
                else:
                    print("Invalid password please try again")
                    continue
        
        elif short_code == "li":
            print("*"*50)
            print("Enter your Username:")
            username = input("Username: ")
            print('*' * 50)
            print("Enter your Password:")
            password = input("password: ")
        
            if login_user(username, password):
                print(f"Hello {username}.Welcome To PassWord Locker Manager")  
                
                while True:
                    print("Use these short codes to choose what to do next:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
                    short_code = input().lower().strip()
                    
                    if short_code == "cc":
                        print("Create New Credential")
                        print("."*20)
                        print("Account name ....")
                        account = input().lower()
                        print("Your Account username")
                        userName = input()
                        while True:
                            print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                            password_Choice = input().lower().strip()
                            if password_Choice == 'tp':
                                password = input("Enter Your Own Password\n")
                                save_credentials(create_new_credential(account,userName,password))
                                print('\n')
                                print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully!")
                                print('\n')
                                break
                            elif password_Choice == 'gp':
                                password = generate_Password()
                                save_credentials(create_new_credential(account,userName,password))
                                print('\n')
                                print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully!")
                                print('\n')
                                break
                            else:
                                print("Invalid password please try again")
                                continue
           
                    elif short_code == "dc":
                        if display_accounts_details():
                            print("Here's your list of accounts: ")
                            print('*' * 30)
                            print('_'* 30)
                            for account in display_accounts_details():
                                print(f" Account:{account.account} \n Username:{username}\n Password:{password}")
                                print('_'* 30)
                                print('*' * 30)
                            continue
                        else:
                            print("You don't have any credentials saved yet....")
                            continue
                    elif short_code == "fc":
                        print("Enter the Account Name you want to search for")
                        search_name = input().lower()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print(f"Account Name : {search_credential.account}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                            print('-' * 50)
                        else:
                            print("That Credential does not exist")
                            print('Make sure you type in correct details!')
                            continue
                    elif short_code == "d":
                        print("Enter the account name of the Credential you want to delete")
                        search_name = input().lower()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print("_"*50)
                            search_credential.delete_credentials()
                            print('\n')
                            print(f"Your stored credential for : {search_credential.account} successfully deleted!!!")
                            print('\n')
                        else:
                            print("That Credential you want to delete does not exist in your database yet!")
                            continue
                    elif short_code == 'gp':
                        password = generate_Password()
                        print(f" {password} Has been generated succesfully. You can proceed to use it to your account")
                    elif short_code == 'ex':
                        print("Thanks for using Password-Locker App.. See you next time!")
                        break
            else:
                print("Invalid Username or Password!")
                print("Please try again!")
                continue
        elif short_code == 'exit':
            print("Thanks for using Password-Locker App.. See you next time!")
            break
        else:
            print("Invalid input!")
            print("Please try again!")
            print('\n')
            continue
    
if __name__ == '__main__':
    passlocker()