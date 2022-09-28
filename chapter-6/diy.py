# Glosary.py
# A Python dictionary can be used to model an actual dictionary.


glosary = {
    "remove()" : "to remove an item by its value",
    "pop()" : "to remove an item from a list but lets you work with that item after removing it",
    "del" : "to permanently remove an item from a list",
    "append()" : "to add new element to the end of a list",
    "insert()" : " to add new element to certain position in a list"     
}


print("I have learn some useful python methods from PYTHON CRASH COURSE: ")
for key, value in sorted(glosary.items()):
    print(" -" + key + " : " + value)

# Add more elements
glosary["for"] = "looping through all values"
glosary["if-elif-else"] = "conditional tests"

print("I have learn some other things from PYTHON CRASH COURSE: ")
for key, value in sorted(glosary.items()):
    print(" -" + key + " : " + value)