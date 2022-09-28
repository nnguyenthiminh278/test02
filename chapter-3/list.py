# The list is a collection of items in a particular order
# [ ] to represent a list

from audioop import reverse


a = list(range(0,11))
print(a)

b = [x for x in range(0,11)] # This is a list comprehension
print(b)
#============== List comprehension ===================================
# newlist = [expression for item in iterable if condition == True] 
b1 = [x*2 + 1 for x in range(0,11)]
print(b1)

b2 = [x for x in range(0,11) if x % 2 == 0]
print(b2)

b3 = [x for x in range(0,11) if x % 2 == 0] + [x for x in range(0,11) if x % 2 != 0]
print(b3)
#=====================================================================
c = [0,1,2,3,4,5,6,7,8,9,10]
print(c)

# You can access any element of the list by its index
print(a[0])

# Use individual element of the list
print(str(a[0]) + " is the element from my list")




# Changing the list
a[0] = -1
print(a)
# adding by appending to the end of the list
a.append("numbers")
print(a)
# adding by inserting to any position of the list
a.insert(0, "free")
print(a)
# Remove an element of the list
# by knowning its position and using del statement
del a[0]
print(a)

# by using pop method to remove the last element of the list and store it in a new variable
a1 = a.pop()
print(a)
print(a1)

# by using pop moethod with the position
a2 = a.pop(0)
print(a)
print(a2)

# by using its value
a.remove(5) # Only remove the 1st occurence of the value, if there's more than 1 similar value , use LOOP
print(a)

a_new = 9
a.remove(a_new)
print(a)


# Organizing a list
d = [0,3,1,2,5,4]
d.sort(reverse=True) # Permanent
print(d)

d1 = [0,3,1,2,5,4]
print(sorted(d1))
d1.reverse()
print(d1)
print(len(d1))


# TRY IT YOURSELF
places = ["japan", "egypt", "usa", "korea", "vietnam"]
print(places)
print(sorted(places))

places.reverse()
print(places)

places.sort()
print(places)
print(len(places))

places.append("uk")
print(places)
places.insert(0, "switzerland")
print(places)
del places[1]
print(places)
places.remove("usa")
print(places)