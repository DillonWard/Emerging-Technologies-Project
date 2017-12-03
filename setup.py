# Used for setting up the application for initial use
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 01/12/2017

# allows for the creation of folders and execution of commands
import os

# checks to see if a directory already exists
#  if it doesnt create a directory for images to be stored in
if not os.path.exists('./images'):
    os.mkdir('./images') 

if not os.path.exists('./data'):
    os.mkdir('./data') 


# runs the command to install node_modules
print("Installing Node Modules")
os.system('npm install')

os.system('clear')

# launches the application
print("Running the Application")

# run the application
os.system('py server.py')