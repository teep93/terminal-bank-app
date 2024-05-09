import getpass
import datetime

welcome_ascii = """
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

menu_printing_separator = '-------------------------------------------------------------------------------'
notification_printing_separator = '*******************************************************************************'
username = ''
password = ''
accounts_and_balance = {'Nhi-Wallet': 5000}
account_list = []
first_name = ''
last_name = ''
logged_in = False
login_counter = 0


def logged_out_menu():
    print(menu_printing_separator)
    print(welcome_ascii) 
    print('1. Create a new account')
    print('2. Log in')
    print('3. Exit')
    print(menu_printing_separator)

def logged_in_menu():
    global first_name, last_name, login_counter, current_datetime
    first_login_message = (f'Welcome back, {first_name} {last_name}! What would you like to do today?')
    general_login_message = (f'What else would you like to do today, {first_name}?')
    login_counter += 1
    if login_counter <= 1:
        print(menu_printing_separator)
        print(first_login_message)
    else:
        print(menu_printing_separator)
        print(general_login_message)
    print('1. View Accounts')
    print('2. Transfer Funds')
    print('3. Open Accounts')
    print('4. Transaction History')
    print('5. Log Out')
    print(menu_printing_separator)

def navigate_menu(logged_in):
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
                view_transactions()    
            elif choice == '5':
                login_counter = 0
                print(notification_printing_separator)
                print('Logging out...')
                print('Successfully logged out.')
                print(notification_printing_separator)
                navigate_menu(logged_in=False)
            else:
                print(notification_printing_separator)
                print('Invalid choice. Please enter 1, 2, 3, 4, or 5.')
                print(notification_printing_separator)
        else:
            if choice == '1':
                create_user_account()
            elif choice == '2':
                log_in()
            elif choice == '3':
                print(notification_printing_separator)
                print('Goodbye!')
                print('Exiting...')
                print(notification_printing_separator)
                exit()
            else:
                print(notification_printing_separator)
                print('Invalid choice. Please enter 1, 2, or 3.')
                print(notification_printing_separator)


def view_accounts():
        print(menu_printing_separator)
        print('Your active accounts and balances.')
        print(accounts_and_balance)
        print(menu_printing_separator)
        while True:
            choice = getpass.getpass('Press any key + ENTER to return to the menu.')
            if choice:
                print('Returning to menu...')
                print(notification_printing_separator)
                break

def transfer_funds():
    global accounts_and_balance
    while True:
        if len(accounts_and_balance) <= 1:
            print('You do not have enough accounts for a transfer.')
            print('Please open more.')
            print(notification_printing_separator)
            break
        else:
            for index, (key, value) in enumerate(accounts_and_balance.items(), start=1):
                print(f'{index}. {key}: ${value}')
            try:
                from_account_index = int(input('Please select an account to transfer FROM: ')) - 1
                to_account_index = int(input('Please select an account to transfer TO: ')) - 1
                transfer_amount = float(input('Enter the amount to transfer: '))
            except ValueError:
                print(notification_printing_separator)
                print('Invalid input. Please enter a valid number')
                print(notification_printing_separator)
                continue
            if not (0 <= from_account_index < len(accounts_and_balance)) or not (0 <= to_account_index < len(accounts_and_balance)):
                print(notification_printing_separator)   
                print('Invalid account selection.')
                print(notification_printing_separator)
                continue
            from_account = list(accounts_and_balance.keys())[from_account_index]
            to_account = list(accounts_and_balance.keys())[to_account_index]
            if transfer_amount <= 0:
                print(notification_printing_separator)
                print('Invalid transfer amount. Please enter positive number.')
                print(notification_printing_separator)
                continue
            if transfer_amount > accounts_and_balance[from_account]:
                print(notification_printing_separator)
                print('Insufficient funds.')
                print(notification_printing_separator)
                continue
            accounts_and_balance[from_account] -= transfer_amount
            accounts_and_balance[to_account] += transfer_amount
            print(notification_printing_separator)
            print('Transfer successful')
            print(notification_printing_separator)
            print(f'Balance for {from_account}: ${accounts_and_balance[from_account]}')
            print(f'Balance for {to_account}: ${accounts_and_balance[to_account]}')
            print(notification_printing_separator)
        choice = getpass.getpass('Press any key + ENTER to return to the menu.')
        if choice:
            print(notification_printing_separator)
            print('Returning to menu...')
            print(notification_printing_separator)
            break            


def open_product_accounts():
    global accounts_and_balance
    print(menu_printing_separator)
    print('Please select an account to open')
    print('1. Transaction Account')
    print('2. Savings Account')
    print('3. Exit')    
    while True:
        choice = input('Please input your choice: ')
        if choice == '1':
            accounts_and_balance['Transaction Account'] = 0
            print(notification_printing_separator)
            print('Transaction Account successfully opened!')
            print(notification_printing_separator)
            break
        elif choice == '2':
            accounts_and_balance['Savings Account'] = 0
            print(notification_printing_separator)
            print('Savings Account successfully opened!')
            print(notification_printing_separator)
            break
        elif choice == '3':
            print(notification_printing_separator)
            print('Returning to menu...')
            print(notification_printing_separator)
            break
        else:    
            print(notification_printing_separator)
            print('Invalid choice. Please enter 1, 2, or 3.')
            print(notification_printing_separator)

def view_transactions():
    pass

    

def log_in():
    global username, password
    print(menu_printing_separator)
    while True:
        input_username = input('Enter your username: ')
        input_password = getpass.getpass('Enter your password: ')
        print(menu_printing_separator)
        if input_username == username and input_password == password:
            print(notification_printing_separator)
            print('Login successful.')
            print(notification_printing_separator)
            navigate_menu(logged_in=True)
            break
        else:
            print(notification_printing_separator)    
            print('Invalid username or password. Please try again.') 
            print(notification_printing_separator)   







def create_user_account():
    global first_name, last_name, username, password
    print('Create an Account')
    first_name = input('Enter your first name: ').capitalize()
    last_name = input('Enter your last name: ').capitalize()
    username = input('Enter desired username: ')
    while True:
        password = getpass.getpass('Enter desired password: ')
        confirm_password = getpass.getpass('Confirm password: ')

        if password == confirm_password:
            print(notification_printing_separator)
            print('Passwords match! Proceeding...')
            print(notification_printing_separator)
            break
        else:
            print(notification_printing_separator)
            print('Passwords do not match. Please try again.')
            print(notification_printing_separator)
    print(notification_printing_separator)
    print('Account successfully created!')
    print(notification_printing_separator)
    print(f'Name: {first_name} {last_name}')
    print(f'Username: {username}')
    print(notification_printing_separator)
    return first_name, last_name, username, password







navigate_menu(logged_in)                             













                        
                




