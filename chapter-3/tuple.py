# Immutable list =  TUPLE

dimention = (200,50)
print("original dimentions are:")
for d in dimention:
    print(d)

dimention = (400,100)
print("\nNew dimentions are:")
for d in dimention:
    print(d)

# TRY IT YOURSHELF
foods = ("rice", "noodle", "bread", "eggs", "vegetable")
print("\nWe offer")
for food in foods:
    print(food)
foods = ("rice", "pasta", "bread", "eggs", "vegetable")
print("\nRevised menu")
for food in foods:
    print(food)


foods = list(foods)
print(foods)
foods.append("apple")
print(foods)



