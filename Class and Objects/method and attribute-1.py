class Dog:
    species = "French Bulldog"

    def __init__(self, name):
        self.name = name

print(Dog.species)

dog1 = Dog('Jack')
print(dog1.name)
print(dog1.species)

dog2 = Dog('Rose')
print(dog2.name)
print(dog2.species)