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

printing_separator = "-------------------------------------------------------------------------------"
username = ''
password = ''
account_list_and_balance = {'Nhi-Wallet': 5000}
first_name = ''
last_name = ''
logged_in = False
login_counter = 0


def logged_out_menu():
    print(printing_separator)
    print(welcome_ascii) 
    print('1. Create a new account')
    print('2. Log in')
    print('3. Exit')
    print(printing_separator)

def logged_in_menu():
    global first_name, last_name, login_counter, current_datetime
    first_login_message = (f'Welcome back, {first_name} {last_name}! What would you like to do today?')
    general_login_message = (f'What else would you like to do today, {first_name}?')
    login_counter += 1
    if login_counter <= 1:
        print(printing_separator)
        print(first_login_message)
    else:
        print(printing_separator)
        print(general_login_message)
    print('1. View Accounts')
    print('2. Transfer Funds')
    print('3. Open Accounts')
    print('4. Transaction History')
    print('5. Log Out')
    print(printing_separator)

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
                print(printing_separator)
                print('Logging out...')
                print('Successfully logged out.')
                print(printing_separator)
                navigate_menu(logged_in=False)
            else:
                print(printing_separator)
                print('Invalid choice. Please enter 1, 2, 3, 4, or 5.')
                print(printing_separator)
        else:
            if choice == '1':
                create_user_account()
            elif choice == '2':
                log_in()
            elif choice == '3':
                print(printing_separator)
                print('Goodbye!')
                print('Exiting...')
                print(printing_separator)
                exit()
            else:
                print(printing_separator)
                print('Invalid choice. Please enter 1, 2, or 3.')
                print(printing_separator)


def view_accounts():
        print(printing_separator)
        print('Your active accounts and balances.')
        print(account_list_and_balance)
        print(printing_separator)
        while True:
            choice = getpass.getpass('Press ENTER to return to the menu.')
            if choice:
                print('Returning to menu...')
                print(printing_separator)
                break
            else:
                break    

def transfer_funds():
    pass

def open_product_accounts():
    global account_list_and_balance
    print(printing_separator)
    print('Please select an account to open')
    print('1. Transaction Account')
    print('2. Savings Account')
    print('3. Exit')    
    while True:
        choice = input('Please input your choice: ')
        if choice == '1':
            account_list_and_balance['Transaction Account'] = 0
            print('Transaction Account successfully opened!')
            print(printing_separator)
            break
        elif choice == '2':
            account_list_and_balance['Savings Account'] = 0
            print('Savings Account successfully opened!')
            print(printing_separator)
            break
        elif choice == '3':
            print('Returning to menu...')
            print(printing_separator)
            break
        else:    
            print(printing_separator)
            print('Invalid choice. Please enter 1, 2, or 3.')
            print(printing_separator)

def view_transactions():
    pass

    

def log_in():
    global username, password
    print(printing_separator)
    while True:
        input_username = input('Enter your username: ')
        input_password = getpass.getpass('Enter your password: ')
        print(printing_separator)
        if input_username == username and input_password == password:
            print(printing_separator)
            print('Login successful.')
            print(printing_separator)
            navigate_menu(logged_in=True)
            break
        else:
            print(printing_separator)    
            print('Invalid username or password. Please try again.') 
            print(printing_separator)   







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
            print("Passwords match! Proceeding...")
            break
        else:
            print("Passwords do not match. Please try again.")
    print(printing_separator)
    print("Account successfully created!")
    print(f'Name: {first_name} {last_name}')
    print(f'Username: {username}')
    print(printing_separator)
    return first_name, last_name, username, password







navigate_menu(logged_in)                             

