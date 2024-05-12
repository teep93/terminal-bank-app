# RorryEvans_T1A3 

[Link to github repo](https://github.com/teep93/terminal-bank-app)

## Project Description

This is a simulated banking application that runs in the terminal. A digital wallet simulates the user's funds outside of the app. Users can create an account, log in, open accounts, withdraw/deposit/transfer funds to/from their wallet and accounts, and view their transaction history.

## Features

### Account Management

![Account Creation](/docs/account-creation.png)
![Log In](/docs/log-in.png)

This feature has a function that will allow the user to create an account with an input prompt. They will enter a first name, last name, username and password which will be stored in global variables.
Global variables are only used for important account information that need to be accessed by functions to display user information (full name), accounts the user has opened, account balances, account
transactions and account information (username and password). Any other variables outside of previous important information will be stored for use in their relevant functions locally.
This feature is mainly handled by the create_user_account() function, it prompts the user to enter their full name, username (which is passed through the capitalize() function before it is stored in the corresponding global variable) and password. A while loop is used to continuously ask the user
for a password and confirmation of password which it then checks if both passwords match before breaking. The getpass package is utilised to stop the echo of the password to the terminal for security purposes and to properly simulate password creation from real banking applications. This also handles the error of making a mistake on the password by confirming it with the user. The function then returns the first name, last name, username and confirmed password global variables.
This feature will also have a function to allow the user to log in to the created account by taking user input and a while loop runs to continuously ask the user for input whilst checking if the username and password is correct by comparing it to the existing user information variables
and if that is correct it will run the navigate menu function and pass in the logged_in variable and evaluating it to True, allowing the user to view the logged in menu. Getpass module is utilised to hide input of any passwords for security purposes. Both functions will print notifications to the user for errors or successful actions. Error handling is managed by the while loop only allowing the user to continue if conditions are 
properly met.


### Persistant Menus and Sub-Menus

![Menu](/docs/menu.png)

This feature has a major function that lets you navigate menu choices and is run by a while loop that handles errors by only letting you choose a valid menu option and running until the user decides to log out which will evaluate the logged_in variable to false and taking the user back to the previous logged out menu. It takes a boolean argument that is only evaluated to True if you successfully log in by showing you the logged out menu or the logged in menu that have different user input choices. Selecting a valid option will then run a corresponding function to either view existing accounts, transfer funds between accounts, opening accounts and logging out. The view existing accounts function will print out a variable that stores a dictionary of current accounts opened and runs a while loop that breaks if you press a key and enter to simulate an account list without returning you to the previous menu. The open product accounts function will run a while loop to keep you in its sub menu by forcing the user to select a type of account and appending that account to the existing account dictionary and giving it a name and value of 0 and breaking the while loop to return you to the previous menu. Any invalid inputs will force the user to choose a valid option or exiting.


### Funds Transfer

![Funds transfer](/docs/transfer-funds.png)

This feature is a major function of the program. It takes the global variable of existing accounts and corresponding key value pairs. It first checks if the user has more than one account otherwise will break the while loop to return you to the previous menu, printing instructions to the user open more accounts. If the user has more than one account it will allow the loop to continue by running a for loop and assigning an index, key and value pair to a local variable of the same names with the enumerate function taking the dictionary's items and starting the index from one for user readability. I have put a try and except block for the following user inputs to select the accounts to transfer from, to, and the amount to handle invalid inputs. User inputs are converted to integers and having 1 subtracted from the integer to account for the starting index and assigned to a corresponding local variable. It will then check those variables (from, to, and amount) if they are valid inputs based on index and length of dictionary. The while loop will continue if so and convert the chosen to and from index variables into a list based off the value of the key (for dollar amounts) and assign those to a variable. The code will check if the transfer amount is valid before letting the user continue and loop back if the amount is invalid. This will then increment (to account) and decrement (from account) to update values that funds have been taken and transferred and will print to the user of the successful transfer and corresponding updated values of the accounts chosen and time completed.


## Implementation Plan

I have used Trello as the professional tool to track the implementation and plan the project.

### Project Management

[Link to Trello for project](https://trello.com/b/euHyLo7m/t1a3-terminal-application)

![Trello](/docs/trello-overview.png)

### Feature 1 - Account Management

![Feature 1](/docs/f1-code.png)
![Feature 1 Docs](/docs/f1-doc.png)

### Feature 2 - Persistent Menus and Sub-Menus

![Feature 2](/docs/f2-code.png)
![Feature 2 Docs](/docs/f2-doc.png)

### Feature 3 - Funds Transfer

![Feature 3](/docs/f3-code.png)
![Feature 3 Docs](/docs/f3-doc.png)

I assigned each feature to a card for either documentation or code with a due date and priority with each feature having at least 5 items on the check list.
I also assigned some rubric requirements to a card of their own.

![Implementation Progress](/docs/implementation-progress.png)

Each card would then be moved to a corresponding column to track whether the task has started, in progress, or completed.

## HELP

### Installation

To run the program, please follow these steps:

Clone the repository:

```bash

git clone https://github.com/teep93/terminal-bank-app.git

```

Navigate to source folder:

```bash

cd src

```

Check if using correct version of python (3.10 or later):

```bash

python3 --version

```

If required, install python3:

```bash

sudo apt update
sudo apt install python3 

```

If in "src" directory, enable script to run:

```bash

chmod +x install.sh

```

Run the install command if first time using program, this will check if virtual environment is setup and if not, will install one:

```bash

source ./install.sh --install

```

If returning to program and already have virtual environment setup:

```bash

source ./install.sh --launch

```

### Dependencies

No external dependencies required.

### System Requirements

Program only requires python 3.10 or higher and a terminal.

## Style Guide

This project follows the PEP8 styling guide.

## References

Rossum, G 2013, PEP 8 – Style Guide for Python Code, Python Enhancement Proposals, viewed 10 May 2024, https://peps.python.org/pep-0008/

Makwana, D, 2023, Automating Virtual Environments: Bash Script Magic For Python Developers, Medium, web log post, 12 August, viewed 11 May 2024, https://makwanadhruv.medium.com/automating-virtual-environments-bash-script-magic-for-python-developers-3a06df1777a6