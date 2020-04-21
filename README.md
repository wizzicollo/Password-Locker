## Project Name
Password-Locker

## Author
Collins Kiprutoh

## Description
This is a project that enable clients to store and retrieve their credentials upon log-in and create new credentials or passwords and even generate random passwords for different accounts.

## Features
 - Create account for new user
 - Logging in
 - Option of computer generated password
 - Create new credential
 - Delete credential
 - Display existing credentials
 - Search credential by site name
 - Copy credential
 - Exit for leaving the site

## Behavior Driven Development
Behavior                |	   Input	                |     Output
on load	                |  loging/signup                | Access to the account
on login	            | show the credential detail	| the store credentials are displayed
Search for credential	| input account	                |credentials with that name displays
option of exit          | 	choose exit option          |	exit


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | In terminal: $./run.py | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | Enter: ca | Enter your first name, last name and password |
| Display prompt for login in | Enter: li | Enter your account name and password |
| Display codes for navigation | Successful login | Choose an option: cc - Create Credential, dc - Display Credentials, fc - Find Credential, cp - Copy Credential, del - Delete Credential, ex - exit |
| Display prompt for creating a credential | Enter: cc | Enter the site name, your username and password |
| Display a list of credentials | Enter: dc | Prints a list of saved credentials |
| Find a credential | Enter: fc | Prints the searched credential |
| Display prompt for which credential to copy | Enter: cp | Enter the site name of the credential you wish to copy. |
| Deletes a saved credential | Enter: del | Prints success |
| Exit application | Enter: ex | Exit the current navigation stage |

## Setup/Installation requirements
 1.Clone or download and unzip the repository from github https://github.com/wizzicollo/Password-Locker.git

2.You can use this command (git clone https://github.com/wizzicollo/Password-Locker.git ) to clone the project to your   machine if you have git .

3.cd into the project folder and open in text editor either code. or atom.

4.Then run chmod +x run.py on your project directory.

5.Run ./run.py to launch the program.


## Technologies Used
 - PYTHON
 - Git

## Contact Information
 - email: kiprutohcollo@gmail.com
 - phone no. : +254 741 280 908