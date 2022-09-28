available_topping = ["mushromms", "olives", "green peppers", "salami", "cheese"]
requested_topping = ["cheese", "chicken"]
for request in requested_topping:
    if request in available_topping:
        print("Adding " + request)
    else:
        print("Sorry, we don't have " + request)
