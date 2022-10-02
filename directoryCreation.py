#!/usr/bin/python3

from os import chdir, mkdir
from subprocess import Popen

current_directory = '/Users/jakewest/Documents/MyProjects'

chdir(current_directory)

project_name = str(input("Enter the project name: "))
try:
    mkdir(current_directory + '/' + '{}'.format(project_name))
except FileExistsError:
    dir = current_directory + '/' + project_name
    print("PROJECT DIRECTORY ALREADY EXISTS")
    Popen(["open", dir])
    exit(1)

new_directory = current_directory + '/' + '{}'.format(project_name)
chdir(new_directory)

while True:
    subDir = str(
        input("Do you want to create any subdirectories? <y/n>\n")).lower()
    if subDir == "y":
        newDir = str(input("What is the name of the subdirectory? "))
        try:
            mkdir(newDir)
        except FileExistsError:
            print("###############That directory already exists###############")
    elif subDir == "n":
        break
    else:
        print("Invalid answer Please enter either <y/n>.\n")

print("Directory created :)")
proc = Popen(["open", new_directory])
