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

    """
    All Starts Here
    """ 

    # Get DB access
    masteruser = input("Enter Master username: ").strip()
    masterpass = getpass.getpass("Enter Master Password: ")

    try:

        # Try accessing to database
        access = DB(masteruser, 'manager', masterpass)

    except Exception as err:

        # Wrong credentials
        print(err)

    else:
        # App Starts Here
        while True:

            # Nice Logo
            printLogo()

            print('Choose one of the following:\n1. Search Password\n2. Add New Password\n3. Delete Password\n4. View Password List\n5. Exit')
            i = input()

            if i == '1':
                # Search for password
                printLogo()
                searchPass(access)

            elif i == '2':
                # Store New Password
                printLogo()
                storePassword(access)

            elif i == '3':
                # Delete Password
                printLogo()
                deletePass(access)

            elif i == '4':
                # Show all passwords stored
                printLogo()
                showList(access)

            elif i == '5':
                # Quit
                clear()
                break

            else:
                # Wrong input
                printLogo()
                print("Wrong Input")


def deletePass(access):
    """Delete a password

    Args:
        access (DB): DB class object
    """    

    print("Enter url and email of the password to be deleted")

    url = input("Enter url: ")
    email = input("Enter email: ")

    access.deleteEntry({'url' : url, 'email' : email})

    print("Deleted! Press enter to continue")

    input()

def showList(access):
    """Show list of passwords in the database

    Args:
        access (DB): DB class object
    """    

    passList = access.getall()

    # Create a table in cmd line
    if passList:
        x = PrettyTable()
        x.field_names = ["URL", "email", "password", "Notes"]

        for i in passList:
            x.add_row(
                [i[2], i[1], '****',i[4]]
            )
        print(x.get_string())

    else:
        # No passwords available
        print('\nNo Passwords Available')

    print('Press enter to exit')
    input()

def searchPass(access):
    """Search for a specific password.

    Args:
        access (DB): DB class object
    """    

    print("Search by url and email")

    email = input("Enter email: ")
    url = input("Enter url: ")

    data = access.getdata({'url' : url, 'email' : email})

    if data:

        # Copy to clipboard
        pyperclip.copy(decrypt(data[3]).decode())
        print("\nCopied to clipboard press ENTER to exit")

    else:
        print("\nNo Matches found. Press enter to go back")

    input()
    

def storePassword(access):
    """Store new password

    Args:
        access (DB): DB class object
    """    

    # Ask if needed to generate new password or just save
    i = input('1. Generate and store password\n2. Just Store the password\n')

    if i == '1':
        # Generate and save
        printLogo()
        genetateNStore(access)

    elif i == '2':
        # Just Save
        printLogo()
        savepass(access)

def genetateNStore(access):
    """Generate and store in Database

    Args:
        access (DB): DB class object
    """    

    while True:

        print("Enter -1 to exit\n")
        # Ask for a len of password > 6
        l = input("Enter Length of password ( > 6): ")

        try:
            # Check if the input is an integer
            t = int(l)

        except:
            # If not integer
            printLogo()
            print("Please enter integer")
        else:
            # If Integer

            if t == -1:
                # Exit
                return

            elif int(l) > 6:
                #  If len > 6
                break

            else:
                # if len < 6
                printLogo()
                print("Please give a length > 6\n")
    
    # Generate password
    password = generator(int(l))
    printLogo()
    # Save the password
    savepass(access, password=password)

def savepass(access, password = ''):
    """encrypt and save the record in the database

    Args:
        access (DB): DB class object
        password (str): Passed if a password is generated. Defaults to ''.
    """    

    # take details
    print('(Not all details are compulsory exept for password, email and url)\nEnter Details:')

    url = input('Url: ')
    username = input('Username: ')
    email = input('Email: ')

    if password == '':
        # If just password
        password = input('Password: ')

    else:
        # If generated password, copied to clipboard 
        print(f"Password: {'*'* len(password)}\nPassword Copied to clipboard")
        pyperclip.copy(password)

    notes = input('Notes: ')
    # If relevant data
    if password and url and email:
        access.savedata({
            'url' : url,
            'username' : username,
            'password' : password,
            'email' : email,
            'notes' : notes
        })
        print("Data Saved!\n Press enter to continue")

    else:
        # If not
        print("Insufficient data submitted. Please try again")

    input()

if __name__ == "__main__":
    # Setup.py takes care of this
    if KEYPATH == '':
        print('Please Run setup.py first')
    elif os.path.exists(KEYPATH):
        main()
    else:
        print('ERROR! Fix KEYPATH in main.py')

