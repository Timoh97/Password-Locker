from string import ascii_letters, punctuation, digits
# import pyperclip
# from secrets import choice
import random
from user import User


class Credentials:
    '''
        Class to create  account credentials, generate passwords and save their information
        '''

    credentials_list = []
    user_credentials_list = []
    
    def __init__(self, social_site, username, password):
        '''
        initializes user properties to hold
        '''
        self.social_site = social_site
        self.username = username
        self.password = password


    def generate_password(self, password_len=8):
        random_str = ascii_letters + punctuation + digits
        password = "".join(choice(random_str) for x in range(password_len))
        # import pdb; pdb.set_trace()
        return password

    @classmethod
    def check_user(cls, first_name, last_name, password):
        '''
            Checks if the password and name exist in list_user
            '''
        current_user = ''

        for user in User.list_user:
            if (user.first_name == first_name) and (user.first_name == last_name) and (user.password == password):
                current_user = user.first_name

        return current_user


    def save_credentials(self):
        '''
            save_credentials adds the credentials of a user to the credentials_list.
            '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
            allows user to delete  credentials from credentials_list
            '''

        self.credentials_list = [
            x for x in self.credentials_list if x["username"] != username]

    def display_credential(self):
        '''
        display_credential this method that retuns the list of credential_list
        '''
        return self.credentials_list

    @classmethod
    def get_for_aSocial_site(cls, social_site):
        '''
            gets credentials for a given social site and returns them
            '''

        for credential in cls.credentials_list:
            if credential in credential.social_site == social_site:
                return credential

    @classmethod
    def pyperclip_copy(cls, social_site):

        get_credentials = Credentials.get_for_aSocial_site(social_site)
        return pyperclip.copy(get_credentials)

    def view_account(self, name):
        for account in self.credentials_list:
            if account['name'] == name:
                return account
