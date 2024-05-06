from menu import Account

class Main:

    def __init__(self):
        pass

    def display_menu(self): 
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
        print(welcome_ascii) 
        print("1. Create a new account")
        print("2. Log in")
        print("3. Exit")
  
    def get_choice(self):
        while True:
            choice = input("Please enter your choice: ")
            if choice in ["1", "2", "3"]:
                return choice
            else:
                print("Error. Please enter 1, 2, or 3.")  

    def create_account(self):
        account = Account.create_account()
        print("Account created Successfully.")
        account.display_account_info()
        

    def log_in(self):
        pass

    def exit(self):
        print("Exiting...")
        exit()

    def run_menu(self):
        while True:
            self.display_menu()
            choice = self.get_choice()
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.log_in()
            elif choice == "3":
                self.exit()






main_menu = Main()
main_menu.run_menu()                                   

