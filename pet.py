# Create a Pet class
class Pet:
    # Constructor that initializes name, species, age, adopted 
    def __init__(self, name, species, age, adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted

