welcome_ascii = """
 __       __            __                                                      __                      __    __  __        __          _______                       __       
|  \  _  |  \          |  \                                                    |  \                    |  \  |  \|  \      |  \        |       \                     |  \      
| $$ / \ | $$  ______  | $$  _______   ______   ______ ____    ______         _| $$_     ______        | $$\ | $$| $$____   \$$        | $$$$$$$\  ______   _______  | $$   __ 
| $$/  $\| $$ /      \ | $$ /       \ /      \ |      \    \  /      \       |   $$ \   /      \       | $$$\| $$| $$    \ |  \ ______ | $$__/ $$ |      \ |       \ | $$  /  \\
| $$  $$$\ $$|  $$$$$$\| $$|  $$$$$$$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\       \$$$$$$  |  $$$$$$\      | $$$$\ $$| $$$$$$$\| $$|      \| $$    $$  \$$$$$$\| $$$$$$$\| $$_/  $$
| $$ $$\$$\$$| $$    $$| $$| $$      | $$  | $$| $$ | $$ | $$| $$    $$        | $$ __ | $$  | $$      | $$\$$ $$| $$  | $$| $$ \$$$$$$| $$$$$$$\ /      $$| $$  | $$| $$   $$ 
| $$$$  \$$$$| $$$$$$$$| $$| $$_____ | $$__/ $$| $$ | $$ | $$| $$$$$$$$        | $$|  \| $$__/ $$      | $$ \$$$$| $$  | $$| $$        | $$__/ $$|  $$$$$$$| $$  | $$| $$$$$$\\
| $$$    \$$$ \$$     \| $$ \$$     \ \$$    $$| $$ | $$ | $$ \$$     \         \$$  $$ \$$    $$      | $$  \$$$| $$  | $$| $$        | $$    $$ \$$    $$| $$  | $$| $$  \$$\\
 \$$      \$$  \$$$$$$$ \$$  \$$$$$$$  \$$$$$$  \$$  \$$  \$$  \$$$$$$$          \$$$$   \$$$$$$        \$$   \$$ \$$   \$$ \$$         \$$$$$$$   \$$$$$$$ \$$   \$$ \$$   \$$
"""

username = ''
password = ''
account_list_and_balance = {}
wallet = 0
firstname = ''
lastname = ''
logged_in = False


def logged_out_menu():
    print(welcome_ascii) 
    print('1. Create a new account')
    print('2. Log in')
    print('3. Exit')

def logged_in_menu():
    print(welcome_ascii)
    print(f'Welcome back, {firstname}! What would you like to do today?')
    print('1. View Accounts')
    print('2. Transfer Funds')
    print('3. Open Accounts')
    print('4. Log Out')

def navigate_menu(logged_in):
    while True:
        if logged_in:
            logged_in_menu()
        else:
            logged_out_menu()    

        choice = input('Please enter your choice: ')

        if logged_in:
            if choice == '1':
                view_accounts()
            elif choice == '2':
                transfer_funds()
            elif choice == '3':
                open_product_accounts()
            elif choice == '4':
                run_logged_out_menu()
            else:
                print('Invalid choice. Please enter 1, 2, 3, or 4.')
        else:
            if choice == '1':
                create_user_account()
            elif choice == '2':
                log_in()
            elif choice == '3':
                exit()
            else:
                print('Invalid choice. Please enter 1, 2, or 3.')


    

def log_in():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == username and password == password:
        print('Login successful.')
        logged_in_menu()
    else:    
        print('Invalid username or password. Please try again.')    

def exit():
    print('Exiting...')
    exit()

def run_logged_out_menu():
    while True:
        logged_out_menu()
        choice = get_choice()


def run_logged_in_menu():
    while True:
        logged_in_menu()
        choice = get_choice()
         



def create_user_account():
    print('Create an Account')
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    username = input('Enter desired username: ')
    password = input('Enter desired password: ')
    print("Account successfully created!")
    print(f'Name: {first_name} + {last_name}, Username: {username}')
    return (first_name, last_name, username, password)

def display_account_info():
    print('Account Information')
    print(f'First Name: {first_name}')
    print(f'Last Name: {last_name}')
    print(f'Username: {username}')
    print(f'Account Balances')





run_logged_out_menu()                                 

