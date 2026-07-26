# Cart নামে একটি Class তৈরি করা হচ্ছে
class Cart:

    # Constructor Method
    # নতুন Cart তৈরি হলে একটি খালি List তৈরি হবে
    def __init__(self):
        self.items = []

    # Cart-এ নতুন Item যোগ করার Method
    def add(self, item):
        self.items.append(item)

    # Cart থেকে Item Remove করার Method
    def remove(self, item):
        # Item থাকলে Remove করবে
        if item in self.items:
            self.items.remove(item)
        # Item না থাকলে Message Return করবে
        else:
            return f"{item} is not in Cart!"

    # Cart-এর সকল Item Return করবে
    def list_items(self):
        return self.items

    # Magic Method (__len__)
    # len(cart) কল করলে মোট Item সংখ্যা Return করবে
    def __len__(self):
        return len(self.items)

    # Magic Method (__getitem__)
    # Index ব্যবহার করে Item Access করা যাবে
    # উদাহরণ: cart[0], cart[2]
    def __getitem__(self, index):
        return self.items[index]

    # Magic Method (__contains__)
    # in Operator ব্যবহার করে Item আছে কিনা পরীক্ষা করবে
    def __contains__(self, item):
        return item in self.items

    # Magic Method (__iter__)
    # Cart-কে Iterable বানাবে, ফলে for Loop ব্যবহার করা যাবে
    def __iter__(self):
        return iter(self.items)


# নতুন Cart Object তৈরি করা হচ্ছে
cart = Cart()

# Cart-এ Item যোগ করা হচ্ছে
cart.add("Apple")
cart.add("Orange")
cart.add("Banana")
cart.add("Jack-Fruit")


# Cart-এর প্রতিটি Item Loop দিয়ে প্রিন্ট করা হচ্ছে
for item in cart:
    print(item, end="  ")

print()

# Cart-এ মোট কতটি Item আছে তা প্রিন্ট করবে
print(len(cart))

# Index 3-এর Item প্রিন্ট করবে
print(cart[3])

# Banana Cart-এ আছে কিনা পরীক্ষা করবে
print("Banana" in cart)

# laptop Cart-এ আছে কিনা পরীক্ষা করবে
print("laptop" in cart)

# Banana Remove করা হচ্ছে
cart.remove("Banana")

# Remove করার পর Cart-এর সকল Item দেখাবে
print(cart.list_items())

# Baanana নামে কোনো Item নেই
# তাই remove() একটি Message Return করবে
print(cart.remove("Baanana"))