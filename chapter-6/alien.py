alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x-position: " + str(alien_0["x_position"]))
alien_0["speed"] = "fast"

# Move to the right with different speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment


print("New position: " + str(alien_0["x_position"]))