class Pet(object):
    def __init__(self, animal, color, food, noise, name):
        self.Animal = animal
        self.Color = color
        self.Food = food
        self.Noise = noise
        self.Name = name


def pet_info(pets):
    for p in pets:
        print(p.Name + " eats " + p.Food)


pets = [Pet("frog", "blue", "fries", "ribbit", "Sparky"), Pet("cat", "red", "fish", "yammo", "Rom")]
pet_info(pets)
