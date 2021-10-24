from user import User
from credentials import Credentials


def main():
    print ("Hi mate! Welcome to password Locker. Enter your first_name")
    first_name=input()
    print("Enter your last_name")
    last_name = input()
    
    
    print("You are a step away from the locker, let's rock. Enter password")
    password=input()
    
    print(f'your first name is {first_name} and password for this account is {password}')
    
    
    print("press 1 to enter new password or 2 to generate password")
    user_code =input()
    
    if user_code ==1:
        password=input("Enter password:")
        confirm_pass=input("confirm password:")
        while password !=confirm_pass:
            print("Does not match")
            confirm_pass = input("Please, confirm password: ")
    else:
        password_len=int(input("Enter length of the password"))
        password=Credentials.generate_password(password_len)
        print(f'The password is generated and it is {password}')
        
        
    print("Congratulations this is password locker, for best password solutions")
    print("\n")
    
    
    account_user = User(first_name,last_name,password)
    
    while 1:
        print("We use min codes for easy navigation:\n  cc-create account \n dsp-display credentials \n del- to delete the account \n ex-to exit")
        
        min_codes = input().lower()
        print("min code is",min_codes)
        
        if min_codes=="cc":
          print("what account do you want to create e.g facebook")
          Account_name =input()
          print("Enter username")
          username=input()
          print("1.enter password\n2 Generated password")
          user_in = int(input())
          if user_in==1:
              password=input ("Enter password:")
          else:
              password_len = int(input("Password length: "))
              password =account_user.generate_password(password_len)
              print("The generated password is {password}")
              account_user.save_credentials(Account_name,username,password)
        elif min_codes=="dsp":
            if account_user.display_credential()!=[]:
                 print("Here are your account credentials")
                 for account in account_user.display_credential():
                     print("\n")
            else:
                print("such account doesn't exist! we are sorry.")
                 
        elif min_codes == "del":
            while 1:
                user_in = input('Enter Account name')
                account_user.delete_credentials(user_in)
                print("Account deleted successfully!")
                
        
        elif min_codes =="ex":
            account_user.logout()
            print("Thank you for using my application")
        else:
            print("Invalid min codes. Use valid codes\n cc-to create account \n dsp-to display account details \n ex-to exit \n and del-to delete account")
        
        
        
        
if __name__ == '__main__':
    main()
