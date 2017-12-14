import random


def check_list(p_prizes):
    # Takes in a list of numbers
    # Returns the boolean True or False
    # Checks to see if all the items in the list are > 0.
    # Details: This function checks to see if list is empty.  Returns True if all items are > 0,
    # False is if at least one item is 0.

    return 0 not in p_prizes


def new_prize(p_prizes):
    # Takes in a list of numbers
    # Returns the list with a new prize added (add 1 to element corresponding to prize chosen)
    # Gets random prize and updates the list to increase the list item representing that prize by 1 and prints the list
    # Details: This function gets a new prize within a particular simulation run.  That is, you start off with a list
    # that looks like [0, 0, 0, 0, 0, 0] and end up with a list that looks like [0, 0, 1, 0, 0, 0] if you got prize #3.

    p_prizes[random.randint(0, len(p_prizes) - 1)] += 1
    return p_prizes


def get_all_prizes():
    # Takes in nothing
    # Returns the number of purchases made
    # Calls new_prize until a list has a value > 0 for all items in the list.
    # Will use new_prize and check_list

    # Details: This function does one particular run of the simulation.  You keep getting new prizes until you have at
    # least one of each item.

    prizes = [0, 0, 0, 0, 0, 0]
    boxes_bought = 0
    while not check_list(prizes):
        new_prize(prizes)
        boxes_bought += 1
    return boxes_bought


def average_list(p_num_list):
    if len(p_num_list) == 0:
        return "list is empty"
    total = 0
    for item in p_num_list:
        total += item
    return total / len(p_num_list)


def min_list(p_num_list):
    if len(p_num_list) == 0:
        return "list is empty"
    minimum = p_num_list[0]
    for item in p_num_list:
        if item < minimum:
            minimum = item
    return minimum


def max_list(p_num_list):
    # Do not use math function
    # Takes in a list
    # Returns a number
    # Finds the maximum number of a list
    # Details: This function finds the maximum number in a list.  The code is not given to you, but the min_list code
    # should help.

    if len(p_num_list) == 0:
        return "list is empty"
    maximum = p_num_list[0]
    for item in p_num_list:
        if item > maximum:
            maximum = item
    return maximum


def run_simulation(p_num_simulations):
    # Takes a number representing the number of simulations to run
    # Returns a list (see details below)
    # This will run the number of simulations the user requested and print the number of boxes each simulation took to
    # get all prizes. It will build a list with each item in the list representing how many purchases it took to get all
    # the prizes in that simulation and return that list.
    # Calls get_all_prizes()
    # Details: This function runs all the simulations.  You will start off with an empty list, and slowly grow it.  If
    # you have to buy 10 boxes to get all six prizes in your first run, the list will look like [10].  If you have to
    # buy thirteen boxes to get all six prizes in your second run, the list will now look like [10, 13 ].  This list
    # will keep growing for each run you do.
    sim_data = []

    # for loop to run p_num_simulations times
    # call get_all_prizes and store the response in a variable
    # use append on sim_data to add the number of purchases on this run of get_all_prizes
    # print the number of boxes and the count of the current simulation

    for i in range(p_num_simulations):
        sim_data.append(get_all_prizes())
    return sim_data


# Uncomment the following lines to test min_list and max_list
# Before you run, ask yourself what do you expect min and max to be?

# test_numbers = [3, 5, 7, 2, 7]
# min = min_list(test_numbers)
# max = max_list(test_numbers)
# print("min is " + str(min))
# print("max is " + str(max))

num_simulations = int(input("How many times to run simulation?"))
simulation_data = run_simulation(num_simulations)
print("The minimum number of purchases was: " + str(min_list(simulation_data)))
print("The maximum number of purchases was: " + str(max_list(simulation_data)))
print("The average number of purchases was: " + str(average_list(simulation_data)))
