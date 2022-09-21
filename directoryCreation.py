#!/usr/bin/python3

from os import chdir, mkdir
from subprocess import call

current_directory = '{ ENTER THE ABSOLUTE PATH TO YOUR DESIRED DIRECTORY HERE }'

chdir(current_directory)

project_name = str(input("Enter the project name: "))
mkdir(current_directory + '/'+ '{}'.format(project_name))

new_directory = current_directory + '/'+ '{}'.format(project_name)
chdir(new_directory)

done = False
while done != True:
    subDir = str(input("Do you want to create any subdirectories? <y/n>\n")).lower()
    if subDir == "y":
        newDir = str(input("What is the name of the subdirectory? "))
        mkdir(newDir)
    elif subDir == "n":
        done = True
        break
    else:
        print("Invalid answer Please enter either <y/n>.\n")

print("Directory created :)")
call(["open", "-R", new_directory])