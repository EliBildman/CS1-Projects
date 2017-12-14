to_do = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": [], "sunday": []}

while True:
    action = input("What would you like to do? ")
    day = input("What day? ")
    if day.lower() in to_do:
        if action == "add":
            activity = input("What would you like to add to " + day +"'s to-do list? ")
            to_do[day.lower()].append(activity)
        elif action == "get":
            print("You have to " + ", ".join(to_do[day.lower()]))