#!/usr/bin/python3

# Nested calls are when a function is called within another function.

num = input("Enter a number: ")
num = float(num)
num = abs(num)  
num = round(num)
print(num)

print(round(abs(float(input("Enter a whole positive integer: "))))) # Nested calls, example of a nested call.