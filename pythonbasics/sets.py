#!/usr/bin/python3

# Sets are unordered collections of unique elements, no duplicates.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes) # Combines two sets.
# dinner_table = utensils.union(dishes) # Combines two sets into a new set.

# print(utensils.difference(dishes)) # Returns the difference between two sets.
print(utensils.intersection(dishes)) # Returns the common elements between two sets.


for x in utensils:
    print(x)
