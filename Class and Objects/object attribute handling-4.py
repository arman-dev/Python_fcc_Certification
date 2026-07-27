# Product নামে একটি Class তৈরি করা হচ্ছে
class Product:

    # Constructor Method
    # Object তৈরি হওয়ার সময় name এবং price সেট করবে
    def __init__(self, name, price):
        self.name = name        # Product-এর নাম সংরক্ষণ করছে
        self.price = price      # Product-এর মূল্য সংরক্ষণ করছে


# Product Class থেকে একটি Object তৈরি করা হচ্ছে
product_1 = Product("T-Shirt", 25)


# Product-এর জন্য প্রয়োজনীয় Attribute-এর একটি List
required_attributes = ["name", "price", "inventory_id"]


# প্রতিটি Required Attribute একে একে পরীক্ষা করা হচ্ছে
for attr in required_attributes:

    # hasattr() ব্যবহার করে দেখা হচ্ছে Attribute টি Object-এ আছে কিনা
    if not hasattr(product_1, attr):

        # Attribute না থাকলে Error Message প্রিন্ট করবে
        print(f"ERROR: Product is missing the required attribute: '{attr}'")

    else:
        # Attribute থাকলে getattr() ব্যবহার করে তার Value বের করবে
        print(f"{attr}: {getattr(product_1, attr)}")