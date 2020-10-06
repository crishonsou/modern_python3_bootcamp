class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f'You can´t have a {species} pet!')
        self.name = name
        self.species = species
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f'You can´t have a {species} pet!')
        self.species = species


cat = Pet('Blue', 'cat')
dog = Pet('Wyatt', 'dog')

print(cat.species)
print(dog.species)
cat.set_species('cat')
print(Pet.allowed)
Pet.allowed.append('pig')
print(Pet.allowed)

