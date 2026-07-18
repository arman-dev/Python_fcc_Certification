products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
for price in products.values():
    print(price)
for Name in products.keys():
    print(Name)
for product in products:
    print(product)


for product in products.items():
    print(product)
for name, price in products.items():
    print(name,":",price)
for name,price in products.items():
    products[name] = round(0.8*price)
print(products)



for product in enumerate(products):
    print(product)
for product,price in enumerate(products):
    print(product,price)
for product in enumerate(products.values()):
    print(product)
for product, price in enumerate(products.values()):
    print(product,price)

for index, product in enumerate(products.items()):
    print(index, product)
for index, product in enumerate(products.items(), 1): #starting value of index
    print(index, product)