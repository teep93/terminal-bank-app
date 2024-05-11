import getpass
import datetime

WELCOME_ASCII = """
 __    __  __        __          _______                       __       
|  \  |  \|  \      |  \        |       \                     |  \      
| $$\ | $$| $$____   \$$        | $$$$$$$\  ______   _______  | $$   __ 
| $$$\| $$| $$    \ |  \ ______ | $$__/ $$ |      \ |       \ | $$  /  \\
| $$$$\ $$| $$$$$$$\| $$|      \| $$    $$  \$$$$$$\| $$$$$$$\| $$_/  $$
| $$\$$ $$| $$  | $$| $$ \$$$$$$| $$$$$$$\ /      $$| $$  | $$| $$   $$ 
| $$ \$$$$| $$  | $$| $$        | $$__/ $$|  $$$$$$$| $$  | $$| $$$$$$\\
| $$  \$$$| $$  | $$| $$        | $$    $$ \$$    $$| $$  | $$| $$  \$$\\
 \$$   \$$ \$$   \$$ \$$         \$$$$$$$   \$$$$$$$ \$$   \$$ \$$   \$$
"""

MENU_PRINTING_SEPARATOR = '-------------------------------------------------------------------------------'
NOTIFICATION_PRINTING_SEPARATOR = '*******************************************************************************'
username = ''
password = ''
accounts_and_balance = {'Nhi-Wallet': 5000}
account_list = []
first_name = ''
last_name = ''
logged_in = False
login_counter = 0
current_datetime = datetime.datetime.now()
formatted_time = current_datetime.strftime('%H:%M')


def logged_out_menu():
    """Initial menu when simulation is started.

    Also the menu that the user is returned to upon logging out of their account.

    This function takes no arguments and does not return anything.
    """
    print(MENU_PRINTING_SEPARATOR)
    print(WELCOME_ASCII) 
    print('1. Create a new account')
    print('2. Log in')
    print('3. Exit')
    print(MENU_PRINTING_SEPARATOR)

def logged_in_menu():
    """The menu that is loaded when a user successfully creates and logs in to an account.

    Uses the login_counter variable to check if user has logged in for the first time or not
    and adjusts the welcome message accordingly. Presents the current time and options for the
    user to select.

    This function takes no arguments and does not return anything.
    """
    global login_counter, first_name, last_name
    first_login_message = (f'Welcome back, {first_name} {last_name}! What would you like to do today?')
    general_login_message = (f'What else would you like to do today, {first_name}?')
    login_counter += 1
    if login_counter <= 1:
        print(MENU_PRINTING_SEPARATOR)
        print(first_login_message)
    else:
        print(MENU_PRINTING_SEPARATOR)
        print(general_login_message)
    print(f'The time is: {formatted_time}')
    print('1. View Accounts')
    print('2. Transfer Funds')
    print('3. Open Accounts')
    print('4. Log out')
    print(MENU_PRINTING_SEPARATOR)

def navigate_menu(logged_in):
    """Persistant menu that checks if user is currently logged in or not.

    It will present 2 different menus depending on whether or not user has
    logged into their account with different choices.

    Args:
        logged_in (bool): When starting the program, logged_in is always set to false
        to help prompt the user to create an account and to simulate a fresh start
        of a banking application. Upon successfully creating an account and logging in,
        logged_in is set to True to allow user to view relevant menu and select options relevant to a
        logged in user. Choosing the log out option will set logged_in to False to take user
        back to the logged_out_menu.

    Return:
        This function does not return anything.    
    """
    while True:
        if logged_in:
            logged_in_menu()
        else:
            logged_out_menu()    

        choice = input('Please enter your choice: ')

        if logged_in:
            global login_counter
            if choice == '1':
                view_accounts()
            elif choice == '2':
                transfer_funds()
            elif choice == '3':
                open_product_accounts()  
            elif choice == '4':
                login_counter = 0
                print(NOTIFICATION_PRINTING_SEPARATOR)
                print('Logging out...')
                print('Successfully logged out.')
                print(NOTIFICATION_PRINTING_SEPARATOR)
                navigate_menu(logged_in=False)
            else:
                print(NOTIFICATION_PRINTING_SEPARATOR)
                print('Invalid choice. Please enter 1, 2, 3, or 4.')
                print(NOTIFICATION_PRINTING_SEPARATOR)
        else:
            if choice == '1':
                create_user_account()
            elif choice == '2':
                log_in()
            elif choice == '3':
                print(NOTIFICATION_PRINTING_SEPARATOR)
                print('Goodbye!')
                print('Exiting...')
                print(NOTIFICATION_PRINTING_SEPARATOR)
                exit()
            else:
                print(NOTIFICATION_PRINTING_SEPARATOR)
                print('Invalid choice. Please enter 1, 2, or 3.')
                print(NOTIFICATION_PRINTING_SEPARATOR)


def view_accounts():
    """Allows user to view current accounts.

    Prints the accounts_and_balance dict that only initially contains their
    wallet and starting funds. As the user chooses to add more accounts, these
    accounts will be viewable.

    This function does not take any arguments and does not return anything.
    """
    print(MENU_PRINTING_SEPARATOR)
    print('Your active accounts and balances.')
    print(accounts_and_balance)
    print(MENU_PRINTING_SEPARATOR)
    while True:
        choice = getpass.getpass('Press any key + ENTER to return to the menu.')
        if choice:
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print('Returning to menu...')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            break

def transfer_funds():
    """Allows the user to transfer funds between accounts.

    Will create a persistant sub-menu that will first check if the user
    has more than one account and check for invalid inputs. This will increment
    and decrement the selected accounts the user chooses to transfer to and from.

    This function does not take any arguments or returns anything.
    """
    global accounts_and_balance
    while True:
        if len(accounts_and_balance) <= 1:
            print('You do not have enough accounts for a transfer.')
            print('Please open more.')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            break
        else:
            for index, (key, value) in enumerate(accounts_and_balance.items(), start=1):
                print(f'{index}. {key}: ${value}')
            try:
                from_account_index = int(input('Please select an account to transfer FROM: ')) - 1
                to_account_index = int(input('Please select an account to transfer TO: ')) - 1
                transfer_amount = float(input('Enter the amount to transfer: '))
            except ValueError:
                print(NOTIFICATION_PRINTING_SEPARATOR)
                print('Invalid input. Please enter a valid number')
                print(NOTIFICATION_PRINTING_SEPARATOR)
                continue
            if not (0 <= from_account_index < len(accounts_and_balance)) or not (0 <= to_account_index < len(accounts_and_balance)):
                print(NOTIFICATION_PRINTING_SEPARATOR)   
                print('Invalid account selection.')
                print(NOTIFICATION_PRINTING_SEPARATOR)
                continue
            from_account = list(accounts_and_balance.keys())[from_account_index]
            to_account = list(accounts_and_balance.keys())[to_account_index]
            if transfer_amount <= 0:
                print(NOTIFICATION_PRINTING_SEPARATOR)
                print('Invalid transfer amount. Please enter positive number.')
                print(NOTIFICATION_PRINTING_SEPARATOR)
                continue
            if transfer_amount > accounts_and_balance[from_account]:
                print(NOTIFICATION_PRINTING_SEPARATOR)
                print('Insufficient funds.')
                print(NOTIFICATION_PRINTING_SEPARATOR)
                continue
            accounts_and_balance[from_account] -= transfer_amount
            accounts_and_balance[to_account] += transfer_amount
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print(f'Transfer successful at {formatted_time}')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print(f'Balance for {from_account}: ${accounts_and_balance[from_account]}')
            print(f'Balance for {to_account}: ${accounts_and_balance[to_account]}')
            print(NOTIFICATION_PRINTING_SEPARATOR)
        choice = getpass.getpass('Press any key + ENTER to return to the menu.')
        if choice:
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print('Returning to menu...')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            break

def open_product_accounts():
    """Allows user to open additional accounts.

    This function does not take any arguments or returns anything.
    """
    global accounts_and_balance
    print(MENU_PRINTING_SEPARATOR)
    print('Please select an account to open')
    print('1. Transaction Account')
    print('2. Savings Account')
    print('3. Exit')    
    while True:
        choice = input('Please input your choice: ')
        if choice == '1':
            accounts_and_balance['Transaction Account'] = 0
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print(f'Transaction Account successfully opened at {formatted_time}!')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            break
        elif choice == '2':
            accounts_and_balance['Savings Account'] = 0
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print(f'Savings Account successfully opened at {formatted_time}!')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            break
        elif choice == '3':
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print('Returning to menu...')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            break
        else:    
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print('Invalid choice. Please enter 1, 2, or 3.')
            print(NOTIFICATION_PRINTING_SEPARATOR)

def log_in():
    """This function will allow the user to log in.

    It takes user inputs to set up a username and password.
    If user input is correct it will evaluate logged_in to True 
    and will allow the user to view the logged in menu.

    This function does not take any arguments or returns anything.
    """
    global username, password
    print(MENU_PRINTING_SEPARATOR)
    while True:
        input_username = input('Enter your username: ')
        input_password = getpass.getpass('Enter your password: ')
        print(MENU_PRINTING_SEPARATOR)
        if input_username == username and input_password == password:
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print('Login successful.')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            navigate_menu(logged_in=True)
            break
        else:
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print('Invalid username or password. Please try again.')
            print(NOTIFICATION_PRINTING_SEPARATOR)


def create_user_account():
    """Allows user to create an account.

    This function takes user input for their full name, username and password.

    This function does not take any arguments.
     
    This function returns the user's names, username and password.

    """
    global first_name, last_name, username, password
    print('Create an Account')
    first_name = input('Enter your first name: ').capitalize()
    last_name = input('Enter your last name: ').capitalize()
    username = input('Enter desired username: ')
    while True:
        password = getpass.getpass('Enter desired password: ')
        confirm_password = getpass.getpass('Confirm password: ')

        if password == confirm_password:
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print('Passwords match! Proceeding...')
            print(NOTIFICATION_PRINTING_SEPARATOR)
            break
        else:
            print(NOTIFICATION_PRINTING_SEPARATOR)
            print('Passwords do not match. Please try again.')
            print(NOTIFICATION_PRINTING_SEPARATOR)
    print(NOTIFICATION_PRINTING_SEPARATOR)
    print('Account successfully created!')
    print(NOTIFICATION_PRINTING_SEPARATOR)
    print(f'Name: {first_name} {last_name}')
    print(f'Username: {username}')
    print(NOTIFICATION_PRINTING_SEPARATOR)
    return first_name, last_name, username, password

navigate_menu(logged_in)          













                        
                




