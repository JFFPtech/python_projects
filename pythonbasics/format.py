#!/usr/bin/python3

# The str.format() method formats the specified value(s) and insert them inside the string's placeholder.

animal = "cow"
item = "moon"

# print("The {} jumped over the {}".format(animal, item)) # The cow jumped over the moon
# print("The {1} jumped over the {0}".format(animal, item)) # The moon jumped over the cow
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon")) # The cow jumped over the cow
print("The {item} jumped over the {item}".format(item="moon", animal="cow")) # The moon jumped over the moon

text = "The {} jumped over the {}"
print(text.format(animal, item)) # The cow jumped over the moon

------------------

number = 3.14159

# print("The number pi is {:.2f}".format(number)) # The number pi is 3.14

number = 1000

print("the number is {:,}".format(number)) # the number is 1,000
print("the number is {:b}".format(number)) # the number is 1111101000
print("the number is {:o}".format(number)) # the number is 1750
print("the number is {:x}".format(number)) # the number is 3e8
print("the number is {:X}".format(number)) # the number is 3E8
print("the number is {:e}".format(number)) # the number is 1.000000e+03
print("the number is {:E}".format(number)) # the number is 1.000000E+03
print("the number is {:g}".format(number)) # the number is 1000
print("the number is {:G}".format(number)) # the number is 1000