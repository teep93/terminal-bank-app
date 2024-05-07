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

printing_seperator = "----------------------------------------------------------------------------------------------"
username = ''
password = ''
account_list_and_balance = {}
wallet = 0
first_name = ''
last_name = ''
full_name = first_name + last_name
logged_in = False


def logged_out_menu():
    print(printing_seperator)
    print(welcome_ascii) 
    print('1. Create a new account')
    print('2. Log in')
    print('3. Exit')
    print(printing_seperator)

def logged_in_menu():
    global first_name, last_name
    print(printing_seperator)
    print(f'Welcome back, {first_name} {last_name}! What would you like to do today?')
    print('1. View Accounts')
    print('2. Transfer Funds')
    print('3. Open Accounts')
    print('4. Log Out')
    print(printing_seperator)

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
                print(printing_seperator)
                print("Logging out...")
                print("Successfully logged out.")
                print(printing_seperator)
                navigate_menu(logged_in=False)
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


def view_accounts():
    if bool(account_list_and_balance):
        print(account_list_and_balance)
    else:
        print(printing_seperator)
        print("You have no accounts") 
        print(printing_seperator)    

def transfer_funds():
    pass

def open_product_accounts():
    pass

    

def log_in():
    global username, password
    input_username = input('Enter your username: ')
    input_password = input('Enter your password: ')
    if input_username == username and input_password == password:
        print('Login successful.')
        navigate_menu(logged_in=True)
    else:    
        print('Invalid username or password. Please try again.')    

def exit():
    print('Exiting...')
    exit()





def create_user_account():
    global first_name, last_name, username, password
    print('Create an Account')
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    username = input('Enter desired username: ')
    password = input('Enter desired password: ')
    print(printing_seperator)
    print("Account successfully created!")
    print(f'Name: {first_name} {last_name}, Username: {username}')
    print(printing_seperator)
    return first_name, last_name, username, password

def display_account_info():
    global first_name, last_name, username
    print('Account Information')
    print(f'First Name: {first_name}')
    print(f'Last Name: {last_name}')
    print(f'Username: {username}')
    print(f'Account Balances')





navigate_menu(logged_in)                             

