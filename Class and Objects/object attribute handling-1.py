# Person নামে একটি Class তৈরি করা হচ্ছে
class Person:

    # Constructor Method
    # Object তৈরি হওয়ার সময় name এবং age সেট করবে
    def __init__(self, name, age):
        self.name = name      # Person-এর নাম সংরক্ষণ করছে
        self.age = age        # Person-এর বয়স সংরক্ষণ করছে


# Person Class থেকে একটি Object তৈরি করা হচ্ছে
person = Person("Rahim", 27)


# getattr() ব্যবহার করে name Attribute-এর মান নেওয়া হচ্ছে
print(getattr(person, "name"))

# getattr() ব্যবহার করে age Attribute-এর মান নেওয়া হচ্ছে
print(getattr(person, "age"))

# city নামে Attribute নেই
# তাই Default Value "Cox'sbazar" Return করবে
print(getattr(person, "city", "Cox'sbazar"))

# User-এর কাছ থেকে কোন Attribute দেখতে চায় তার নাম ইনপুট নেওয়া হচ্ছে
attr_name = input("Enter the attribute you want to see: ")

# getattr() ব্যবহার করে User-এর দেওয়া Attribute-এর মান বের করা হচ্ছে
# যদি Attribute না থাকে, তাহলে "Attribute not found" Return করবে
print(getattr(person, attr_name, "Attribute not found"))