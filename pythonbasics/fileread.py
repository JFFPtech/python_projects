#!/usr/bin/python3

import modules as mod

try:
    with open("example.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found :(")

mod.hello()