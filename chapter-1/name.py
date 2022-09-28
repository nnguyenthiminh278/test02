# Changing case

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Combining or Concatenating strings
first_name = "ada"
last_name  = "lovelace"
full_name  = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# Add tab (\t) or make a new line (\n) to your text
print("\tPython")
print("Full name:\n\tThi Minh Nghia Nguyen")

# Stripping whitespace with rstrip() method
favorite_language = ' python '
favorite_language
favorite_language.rstrip() # rstrip method removes space temporarily
favorite_language.lstrip()
favorite_language.strip()
