favorit_language = {
    "nghia" : "python",
    "marina" : "ansible",
    "janine" : "python"
}
print(
    "Nghia's favorit language is " + 
    favorit_language["nghia"].capitalize() + 
    "."
)

bac = {
    "gender" : "male",
    "last_name": "nguyen",
    "age" : 33,
    "job" : "it"
}
print(
    "Bac's last name is " + bac["last_name"].capitalize() +
    ". He is " + str(bac["age"]) + " years old. His job is " +
    bac["job"].upper() + "."
)

# looping through pairs of key-value
for key, value in bac.items():
    print("\nKey: " + key.capitalize())
    print("\nValue: " + str(value).upper())


for key in bac.keys():
    print(
        "We have such information: " + key.title()
    )

for key in bac:
    print(
        "We have such information: " + key.title()
    )

# Looping through all keys in order
for name in sorted(favorit_language):
    print(name.title() + ", thank you!")

# Looping through all values
print("The following language are the most famous one: ")
for language in sorted(favorit_language.values()):
    print(language)

# To see the values without repitition
print("We like such languages")
for language in set(favorit_language.values()):
    print(language) 