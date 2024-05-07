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
wallet = None


def logged_out_menu():
    print(welcome_ascii) 
    print('1. Create a new account')
    print('2. Log in')
    print('3. Exit')

def logged_in_menu():
    print(welcome_ascii)
    print('1. View Accounts')
    print('2. Transfer Funds')
    print('3. Open Accounts')
    print('4. Log Out')

def get_choice():
    while True:
        choice = input('Please enter your choice: ')
        if choice in ['1', '2', '3']:
            return choice
        else:
            print('Error. Please enter 1, 2, or 3.')  

    

def log_in():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    for account in created_account:
        if username == username and password == password:
            print('Login successful.')
            self.user_logged_in = True
            return
    print('Invalid username or password. Please try again.')    

def exit(self):
    print('Exiting...')
    exit()

def run_logged_out_menu():
    while True:
        logged_out_menu()
        choice = get_choice()
        if choice == '1':
            create_account()
        elif choice == '2':
            log_in()
        elif choice == '3':
            exit()

def run_logged_in_menu():
    while True:



def create_account():
    print('Create an Account')
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    username = input('Enter desired username: ')
    password = input('Enter desired password: ')
    return (first_name, last_name, username, password)

def display_account_info(self):
    print('Account Information')
    print(f'First Name: {self.first_name}')
    print(f'Last Name: {self.last_name}')
    print(f'Username: {self.username}')





main_menu = Main()
main_menu.run_menu()                                   

