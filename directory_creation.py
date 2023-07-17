"""
Creates a project directory with n-number of subdirectories
"""
#!/usr/bin/python3

import sys
from os import chdir, makedirs, mkdir
from subprocess import Popen

CURRENT_DIRECTORY = '<ENTER THE ABSOLUTE PATH TO YOUR DESIRED DIRECTORY HERE>'

chdir(CURRENT_DIRECTORY)

PROJECT_NAME = str(input("Enter the project name: "))
try:
    mkdir(f"{CURRENT_DIRECTORY}/{PROJECT_NAME}")
except FileExistsError:
    print("PROJECT DIRECTORY ALREADY EXISTS")
    Popen(["open", CURRENT_DIRECTORY + '/' + PROJECT_NAME])
    sys.exit()

NEW_DIRECTORY = f"{CURRENT_DIRECTORY}/{PROJECT_NAME}"
chdir(NEW_DIRECTORY)

while True:
    SUB_DIR = str(
        input("Do you want to create any subdirectories? <y/n>\n")).lower()
    if SUB_DIR == "y":
        NEW_SUB_DIR = str(input(
            "What is the name of the subdirectory?\nNOTE: Multiple sub-directories are supported.\n"))
        try:
            makedirs(NEW_SUB_DIR)
        except FileExistsError:
            print("###############That directory already exists###############")
    elif SUB_DIR == "n":
        break
    else:
        print("Invalid answer Please enter either <y/n>.\n")

print("Directory created :)")
proc = Popen(["open", NEW_DIRECTORY])
