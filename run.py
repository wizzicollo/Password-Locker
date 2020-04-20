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
