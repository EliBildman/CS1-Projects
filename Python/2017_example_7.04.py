import random

class Pokemon(object):
    def __init__(self, name, health_points, attack_power_upper_range, attack_power_lower_range):
        self.name = name
        self.health_points = health_points
        self.attack_power_lower_range = attack_power_lower_range
        self.attack_power_upper_range = attack_power_upper_range

    def attack(self):
        return random.randint(self.attack_power_lower_range, self.attack_power_upper_range)

    def defend(self, enemy, attack_power):
        self.health_points -= attack_power

    def growl(self):
        print("Growl")


class WaterType(Pokemon):
    def growl(self):
        print("Splish Splosh")

    def defend(self, enemy, attack_power):
        if isinstance(enemy, FireType):
            print("It's not very effective.")
            attack_power /= 2
        elif isinstance(enemy, GrassType):
            print("It's super effective!")
            attack_power *= 2


class GrassType(Pokemon):
    def growl(self):
        print("Cheep Cheep")

    def defend(self, enemy, attack_power):
        if isinstance(enemy, WaterType):
            print("It's not very effective.")
            attack_power /= 2
        elif isinstance(enemy, FireType):
            print("It's super effective!")
            attack_power *= 2


class FireType(Pokemon):
    def growl(self):
        print("Fire Fire")

    def defend(self, enemy, attack_power):
        if isinstance(enemy, GrassType):
            print("It's not very effective.")
            attack_power /= 2
        elif isinstance(enemy, WaterType):
            print("It's super effective!")
            attack_power *= 2