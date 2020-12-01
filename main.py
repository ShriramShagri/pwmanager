from src import *
import getpass
import os
from sys import platform
import pyperclip
from prettytable import PrettyTable

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
        while True:
            printLogo()
            print('Choose one of the following:\n1. Search Password\n2. Add New Password\n3. Delete Password\n4. View Password List\n5. Exit')
            i = input()
            if i == '1':
                # Search for password
                printLogo()
                searchPass(access)
            elif i == '2':
                printLogo()
                storePassword(access)
            elif i == '3':
                printLogo()
                deletePass(access)
            elif i == '4':
                printLogo()
                showList(access)
            elif i == '5':
                clear()
                break
            else:
                printLogo()
                print("Wrong Input")


def deletePass(access):
    print("Enter urlandemail of the password to be deleted")
    url = input("Enter url: ")
    email = input("Enter email: ")
    access.deleteEntry({'url' : url, 'email' : email})
    print("Deleted! Press enter to continue")
    input()

def showList(access):
    passList = access.getall()
    if passList:
        x = PrettyTable()
        x.field_names = ["URL", "email", "password", "Notes"]
        for i in passList:
            x.add_row(
                [i[2], i[1], '****',i[4]]
            )
        print(x.get_string())
    else:
        print('\nNo Passwords Available')
    print('Press enter to exit')
    input()

def searchPass(access):
    print("Search by url and email")
    email = input("Enter email: ")
    url = input("Enter url: ")
    data = access.getdata({'url' : url, 'email' : email})
    if data:
        pyperclip.copy(decrypt(data[3]).decode())
        print("\nCopied to clipboard press ENTER to exit")
    else:
        print("\nNo Matches found. Press enter to go back")
    input()
    


def storePassword(access):
    i = input('1. Generate and store password\n2. Just Store the password\n')
    if i == '1':
        printLogo()
        genetateNStore(access)
    elif i == '2':
        printLogo()
        savepass(access)

def genetateNStore(access):
    while True:
        print("Enter -1 to exit\n")
        l = input("Enter Length of password ( > 6): ")
        try:
            t = int(l)
        except:
            printLogo()
            print("Please enter integer")
        else:
            if t == -1:
                return
            elif int(l) > 6:
                break
            else:
                printLogo()
                print("Please give a length > 6\n")
    
    password = generator(int(l))
    printLogo()
    savepass(access, password=password)

def savepass(access, password = ''):
    print('(Not all details are compulsory exept for password, email and url)\nEnter Details:')
    url = input('Url: ')
    username = input('Username: ')
    email = input('Email: ')
    if password == '':
        password = input('Password: ')
    else:
        print(f"Password: {'*'* len(password)}\nPassword Copied to clipboard")
        pyperclip.copy(password)
    notes = input('Notes: ')
    if password and url and email:
        access.savedata({
            'url' : url,
            'username' : username,
            'password' : password,
            'email' : email,
            'notes' : notes
        })

if __name__ == "__main__":
    if KEYPATH == '':
        print('Please Run setup.py first')
    elif os.path.exists(KEYPATH):
        main()
    else:
        print('ERROR! Fix KEYPATH in main.py')

