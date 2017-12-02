import os

# checks to see if a directory already exists
#  if it doesnt create a directory for images to be stored in
if not os.path.exists('./images'):
    os.mkdir('./images') 

# runs the command to install node_modules
print("Installing Node Modules")
os.system('npm install')

os.system('clear')

# launches the application
print("Running the Application")
os.system('py server.py')