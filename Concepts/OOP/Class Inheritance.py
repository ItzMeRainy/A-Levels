# Create parent class Animal.
class Animal:
    def __init__(self, species, habitat, color):
        self.species = species
        self.habitat = habitat
        self.color = color

    # Getter for Species attribute.
    def GetSpecies(self):
        return self.species
    
    # Method to put animal to sleep.
    def Sleep(self):
        print(f"{self.species} is now Sleeping")

# Example 1: Create child class Bird (All attributes/properties and methods are copied from parent).
class Bird(Animal):
    # By using pass, you are copying everything from the parent class
    pass

# Example 2: Create child class Finch (We want to set the species attribute manually since we already know it from the class name, also adding a name for the finch).
class Finch(Bird):
    # This initialization will override the "__init__" from the parent class.
    def __init__(self, name, habitat, color):
        self.species = "Finch"
        self.name = name
        self.habitat = habitat
        self.color = color

    # Adding additional method to this class (This will add to the rest of the already made methods and will not override them).
    def Fly(self):
        print(f"{self.species} named {self.name} is now Flying")

# The relationship between these classes is "Animal ---> Bird ---> Finch" where each next one is the child of the last.
        
# Another way to copy attributes/properties and methods from a parent class is using the "super()" method.
class Fish(Animal):
    def __init__(self, species, habitat, color):
        super().__init__(species, habitat, color)

# This eliminates the need to mention the parent classes name like so.
class Reptile(Animal):
    def __init__(self, species, habitat, color):
        Animal.__init__(species, habitat, color)

'''
super().ExampleFunction(ExampleParameter, ExampleParameter) copies the code from inside the parents similarly named function (in this case it would be named ExampleFunction) and runs it for the child class.

You can also add more code after calling the super method. As an example, we will add the size of the Finch to the Finch class. 
'''

class SizedFinch(Finch):
    def __init__(self, name, habitat, color, size):
        super().__init__(name, habitat, color)
        self.size = size