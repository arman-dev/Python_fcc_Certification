class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def description(self):
        return (f"Color: {self.color} , Model: {self.model}")

obj1 = Car('Red', 'BMW')
obj2 = Car('Black', 'Toyota')

print(obj1.color)
print(obj1.model)
print(obj1.description())

print(obj2.color)
print(obj2.model)
print(obj2.description())

