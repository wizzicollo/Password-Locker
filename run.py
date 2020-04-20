#!/usr/bin/env python3.6
from password import User, Credential
import random
import string
import getpass



def create_user(name, user_password):
    """
    Parameters
    ----------
    name
    user_password
    Returns
    -------
    """
    new_user = User(name, user_password)
    return new_user


def generate_password(user):
    """
    function to generate random password for user
    ----------
    user
    Returns
    -------
    """
    return user.generate_random_password()


def save_user(user):
    """
    Function to save user
    ----------
    user
    """
    user.save_user()


def delete_user(user):
    """
    Function to delete user
    ----------
    user
    """
    user.delete_user()

def create_credential(account, account_username, account_password):
    """
    Parameters
    ----------
    name
    credential_password
    Returns
    -------
    """
    new_credential = Credential(account, account_username, account_password)
    return new_credential


def save_credential(credential):
    """
    Function to save user
    ----------
    user
    """
    credential.save_credential()


def delete_credential(credential):
    """
    Function to delete credential
    ----------
    credential
    """
    credential.delete_credential()


def find_credential(account_username):
    """
    Function to find credential
    ----------
    name
    Returns
    -------
    """
    return Credential.find_by_account_username(account_username)


def check_existing_credentials(account_username):
    """
    Function to check existing credential
    ----------
    name
    Returns
    -------
    user
    """
    return Credential.find_by_account_username(account_username)


def display_credentials():
    """
    Function to display credential
    Returns
    -------
    """
    return Credential.display_all_credentials()


def main():
    """
    Returns
    -------
    """
    # global account_password
    user_name = input("Enter your name > ")

    print(f"Hello {user_name}, welcome to password locker")
    print("\n")
    ask = input(f"Hello {user_name}. Do you have an Account? YES/N0 > ").lower()

    if ask == "no":
        print("Signup with password locker to have access")
        user_name = input("Enter your User name > ")
        create = input(
            f"Hello {user_name}. Do you want a generated password? YES/N0 > ")
        if create == "no":
            print("-"*87)
            print("|Don't mind if your password is not visible as you type. WE go your password secured.|")#
            print("-"*87)
            getpass.getpass()
            print("YOU ARE NOW LOGGED IN")


        while True:
            print("""
            USE THE SHORT CODES
    1. cc - to create a new credential
    2. dc - to display credential
    3. fc - to find credential
    4. dl - to delete credential
    5. gp - to generate a random password
    6. ex- to exit 
            """)
            short_code = input("Use short-codes to navigate > ").lower()
      