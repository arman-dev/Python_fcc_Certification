celsius = [0, 10, 20, 30, 40]
def to_farenheit(temp):
    return (temp*9/5)+32
farenheit = list(map(to_farenheit, celsius))
print(farenheit)