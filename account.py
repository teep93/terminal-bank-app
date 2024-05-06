
class Account:

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    @staticmethod
    def create_account():
        print("Create an Account")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        username = input("Enter desired username: ")
        password = input("Enter desired password: ")
        return Account(first_name, last_name, username, password)
    
    def display_account_info(self):
        print("Account Information")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
