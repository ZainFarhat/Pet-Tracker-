# Create a Pet class
class Pet:
    #Constructor that initializes name, species, age, adopted 
    def __init__(self, name, species, age, adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted

# Method to display_info() → prints all pet data in a readable sentence.
    def display_info(self):
        print(f"{self.name} is a {self.age}-year-old {self.species}. Adopted: {self.adopted}")

#Method mark_adopted() → sets adopted to True.
    def mark_adopted(self):
        self.adopted = True