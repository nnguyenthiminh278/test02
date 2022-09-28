# range() function is used to generate a serie of numbers (object)

a = range(10,20,2)
print(a)
a = str(a)
print(a)

for number in range(1,5):
    print(number)

# To convert to a list
numbers = list(range(0,6))
print(numbers)
even_numbers = list(range(0,6,2))
print(even_numbers)

squares = []
for value in range(0,6):
    square = value **2
    print(str(value) +" ^2 =" + str(square) )
    squares.append(square)
print(squares)
print(sum(squares))

squares_2 = [square**2 for square in range(0,6)]
print(squares_2)

# TRY IT YOURSELF
for num in range(1,21):
    print(num)

new_nums = []
for num in range(1,1001):
    new_nums.append(num)
print(sum(new_nums))

for num in range(1,21,2):
    print(num)

threes = [num * 3 for num in range(3,31)]
print(threes)


# Slice
numbers = range(0,10)
print(numbers[0:3])
print(numbers[1:4])
print(numbers[-2:])
for number in numbers[1:5]:
    print(number)

# Copy list
animes = ["once piece",  "naruto", " demon slayers"]
my_animes = animes[:]
my_animes.append("doraemon")

animes = my_animes
print(animes)
print(my_animes)