# RorryEvans_T1A3 

## Project Description
This is a simulated banking application that runs in the terminal. A digital wallet simulates the user's funds outside of the app. Users can create an account, log in, open accounts, withdraw/deposit/transfer funds to/from their wallet and accounts, and view their transaction history.

## Features

### Account Management

![Account Creation](/docs/account-creation.png){: style="float: left; width: 50%;"}
![Log In](/docs/log-in.png){: style="float: right; width: 50%;"}

This feature will allow the user to create an account with an input prompt. They will enter a first name, last name, username and password which will be stored in global variables.
Global variables are only used for important account information that need to be accessed by functions to display user information (full name), accounts the user has opened, account balances, account
transactions and account information (username and password). Any other variables outside of previous important information will be stored for use in their relevant functions locally.
This feature is mainly handled by the create_user_account() function, it prompts the user to enter their full name, username (which is passed through the capitalize() function before it is stored in the corresponding global variable) and password. A while loop is used to continuously ask the user
for a password and confirmation of password which it then checks if both passwords match before breaking. The getpass package is utilised to stop the echo of the password to the terminal for security purposes and to properly simulate password creation from real banking applications. This also handles the error of making a mistake on the password by confirming it with the user. The function then returns the first name, last name, username and confirmed password global variables. 
!


### Login to Existing Account

### Transaction Historygit

