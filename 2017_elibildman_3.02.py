import random


def birthday_song(name):
    print("Happy birthday to you.")
    print("Happy birthday to you.")
    print("Happy birthday dear " + name + ".")
    print("Happy birthday to you.")


def five_random_cards():
    number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    print(number[random.randint(0, len(number) - 1)] + " of " + suit[random.randint(0, len(suit) - 1)])
    print(number[random.randint(0, len(number) - 1)] + " of " + suit[random.randint(0, len(suit) - 1)])
    print(number[random.randint(0, len(number) - 1)] + " of " + suit[random.randint(0, len(suit) - 1)])
    print(number[random.randint(0, len(number) - 1)] + " of " + suit[random.randint(0, len(suit) - 1)])
    print(number[random.randint(0, len(number) - 1)] + " of " + suit[random.randint(0, len(suit) - 1)])


birthday_song("Eli")
five_random_cards()
