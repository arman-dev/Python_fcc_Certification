class Book:
    def __init__(self, title, page):
        self.title = title
        self.page = page

obj1 = Book('Red Dragon', 230)
obj2 = Book('Anna Careninna', 230)

try:
    print(len(obj1))
except:
    print('Ignore')
print(len(obj1.title))

print(str(obj1))
print(str(obj1.page))

print(obj1 == obj2)
print(obj1.page == obj2.page)