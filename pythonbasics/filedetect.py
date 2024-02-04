#!/usr/bin/python3

import os

path = "/home/username/python_projects/pythonbasics"

if os.path.exists(path):
    print("That location exists")
else:
    print("That location does not exist")

if os.path.isfile(path):
    print("That is a file")
else:   
    print("That is not a file")

if os.path.isdir(path):
    print("That is a directory")
else:   
    print("That is not a directory")