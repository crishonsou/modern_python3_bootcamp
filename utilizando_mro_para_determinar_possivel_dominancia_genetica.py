class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"



class Child(Mother, Father):
    pass




child = Child()
print(child.eye_color)
print(child.hair_color)
print(child.hair_type)



# Mother
#   dominat traits
#   eye_color = "brown"
#   hair_color = "dark brown"
#   hair_type = "curly"

# Father
#    recessive traits
#   eye_color = "blue"
#   hair_color = "blond"
#   hair_type = "straight"
