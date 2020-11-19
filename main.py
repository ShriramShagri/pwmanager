from src.logo import getlogo
from src import *
import getpass
import os
from sys import platform

cmd = ''

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
                break
            else:
                os.system(cmd)
                print(getlogo() +'\n\n')
                print("Wrong Input")

def storePassword(access):
    i = input('\n1. Generate and store password\n2. Just Store the password\n')
    if i == '1':
        pass
    elif i == '2':
        os.system(cmd)
        print(getlogo() +'\n\n')
        savepass(access)

def savepass(access):
    print('(Not all details are compulsory exept for password and url)\nEnter Details:')
    url = input('Url: ')
    username = input('Username: ')
    email = input('Email: ')
    password = input('Password: ')
    notes = input('Url: ')
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


main()

