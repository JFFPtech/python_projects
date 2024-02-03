#!/usr/bin/python3

# **kwargs is a keyword argument that allows you to pass a variable number of keyword arguments to a dictionary.

def hello(**kwargs):
    print("Hello", + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title= "Dr" first='John', middle="Dude", last='Doe') # Hello John Doe