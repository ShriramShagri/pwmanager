from src import *
import getpass
import os
from sys import platform
import pyperclip

cmd = ''
KEYPATH = os.getcwd()

if platform == "linux" or platform == "linux2":
    cmd = 'clear' # Linux
elif platform == "win32":
    cmd = 'cls' # Windows

def main():
    masteruser = input("Enter Master username: ").strip()
    masterpass = getpass.getpass("Enter Master Password: ")

    try:
        access = DB(masteruser, 'manager', masterpass)
    except Exception as err:
        print(err)
    else:
        os.system(cmd)
        print(getlogo() +'\n\n')

        while True:
            
            print('Choose one of the following:\n1. Search Password\n2. Add New Password\n3. Exit')
            i = input()
            if i == '1':
                # Search for password
                pass
            elif i == '2':
                os.system(cmd)
                print(getlogo() +'\n\n')
                storePassword(access)
            elif i == '3':
                os.system(cmd)
                break
            else:
                os.system(cmd)
                print(getlogo() +'\n\n')
                print("Wrong Input")

def storePassword(access):
    i = input('1. Generate and store password\n2. Just Store the password\n')
    if i == '1':
        os.system(cmd)
        print(getlogo() +'\n\n')
        genetateNStore(access)
    elif i == '2':
        os.system(cmd)
        print(getlogo() +'\n\n')
        savepass(access)

def genetateNStore(access):
    while True:
        l = input("Enter Length of password ( > 6): ")
        try:
            t = int(l)
        except:
            os.system(cmd)
            print(getlogo() +'\n\n')
            print("Please enter integer")
        else:
            if int(l) > 6:
                break
            else:
                os.system(cmd)
                print(getlogo() +'\n\n')
                print("Please give a length > 6\n")
    
    password = generator(int(l))
    os.system(cmd)
    print(getlogo() +'\n\n')
    savepass(access, password=password)

def savepass(access, password = ''):
    print('(Not all details are compulsory exept for password and url)\nEnter Details:')
    url = input('Url: ')
    username = input('Username: ')
    email = input('Email: ')
    if password == '':
        password = input('Password: ')
    else:
        print(f"Password: {password}")
    notes = input('Notes: ')
    if password and url:
        access.savedata({
            'url' : url,
            'username' : username,
            'password' : password,
            'email' : email,
            'notes' : notes
        })
    
    os.system(cmd)
    print(getlogo() +'\n\n')


if __name__ == "__main__":
    if KEYPATH == '':
        print('Please Run setup.py first')
    elif os.path.exists(KEYPATH):
        main()
    else:
        print('ERROR! Fix KEYPATH in main.py')

