
cars = ["audi", "bmw", "toyota"]
print(cars)
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


for car in cars:
    if car != "bmw":
        print(car.capitalize())
    else:
        print(car)

# age = 22

# if age < 21:
#     print(True)
# else:
#     print(False)


# age_0 = 31
# age_1 = 33
# if age_0 > 11 and age_1 < 50:
#     print(True)

# for car in cars:
#     print("Is it true that you have BMW?")
#     print(car == "bmw")


# if "vinfast" not in cars:
#     print(True)

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# age = 19
# if age <= 4:
#     price = 0
# elif 4 < age < 30:
#     price = 15 
# else:
#     price = 10
# print(" your cost is " + str(price) +"$")  

# TRY IT YOURSELF

alien_colors = ["green", "red", "violet", "yellow"]

for color in alien_colors:
    if color == "green":
        print("You win 5 points!")
    elif color == "yellow":
        print("You win 7 points")
    else:
        print("You win 10 points")

age = 31
if age < 2:
    print("You are just a baby!")
elif 2 <= age < 4:
    print("You are now a toddler!")
elif 4 <= age < 13:
    print("You are a kid!")
elif 13 <= age < 20:
    print("You are a teenager!")
elif 20 <= age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")


