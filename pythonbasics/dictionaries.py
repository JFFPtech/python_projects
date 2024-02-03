#!/usr/bin/python3

# Dictionaries are unordered mappings for storing objects. They use key-value pairs, fast because they use hashing. They are mutable.

capitals = {"USA":"Washington D.C.", "India":"New Delhi", "China":"Beijing", "Russia":"Moscow"}

capitals.update({"Japan":"Tokyo"}) # Adds a new key-value pair to the dictionary.
capitals.update({"USA":"Massachusetts"}) # Updates the value of the key "USA" to "Massachusetts".
capitals.pop("India") # Removes the key-value pair from the dictionary.
capitals.clear() # Clears the dictionary.

#print(capitals.get('Japan'))
#print(capitals['Russia'])
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items()) # Returns the entire dictionary.

for key, value in capitals.items():
    print(key, value) # Prints the key-value pairs of the dictionary. 