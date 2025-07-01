# Create a Pet class

class Pet:
    # Constructor that initializes name, species, age, adopted 
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

# Method: birthday() → increases the pet's age by 1 year.

    def birthday(self):
        self.age += 1


# Create at least 3 pet objects .

pet1 = Pet("low", "Cat", 3)
pet2 = Pet("Zaatar", "Dog", 2)
pet3 = Pet("Shaq", "Hamster", 1)

# Call their methods and print results to verify 

pet1.display_info()
pet2.display_info()

pet3.mark_adopted()
pet3.display_info()

# Create a list of all pets

pets = [pet1, pet2, pet3]

# Find  non adopted

def find_non_adopted(pets):
    non_adopted = []
    for pet in pets:
        if not pet.adopted:
            non_adopted.append(pet)
    return non_adopted


