#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import os
import subprocess

current_directory = '{ ENTER YOUR DESIRED DIRECTORY HERE }'

os.chdir(current_directory)

name = str(input("Enter the project name: "))
os.mkdir(current_directory + '/'+ '{}'.format(name))

new_directory = current_directory + '/'+ '{}'.format(name)
os.chdir(new_directory)

done = False
while done != True:
    subDir = str(input("Do you want to create any subdirectories? <y/n>\n"))
    subDir.lower()
    if subDir == "y":     
        newDir = str(input("What is the name of the subdirectory? "))
        os.mkdir(newDir)
    elif subDir == "n":
        done = True
        break
    else:
        print("Invalid answer.\n")

print("Directory created.")
subprocess.call(["open", "-R", new_directory])