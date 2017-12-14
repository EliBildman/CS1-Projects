to_do = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": [], "sunday": []}

while True:
    action = input("What would you like to do (add day activity OR get day)? ")
    action = action.split(" ")
    if action[1].lower() in to_do:
        if action[0] == "add":
            is_dup = False
            for day in to_do:
                for activity in to_do[day]:
                    if activity == action[2]:
                        is_dup = True
            if not is_dup:
                to_do[action[1].lower()].append(action[2])
            else:
                print("Sorry that is a duplicate!")
        elif action[0] == "get":
            print("You have to " + ", ".join(to_do[action[1].lower()]))