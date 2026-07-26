# Dog নামে একটি Class তৈরি করা হচ্ছে
class Dog:

    # Class Variable
    # এই Variable সকল Dog Object-এর জন্য একই থাকবে
    species = "French Bulldog"

    # Constructor Method
    # Object তৈরি হওয়ার সময় Dog-এর নাম সেট করবে
    def __init__(self, name):
        self.name = name      # Object Variable (Instance Variable)


# Class Variable সরাসরি Class-এর মাধ্যমে Access করা হচ্ছে
print(Dog.species)


# প্রথম Dog Object তৈরি করা হচ্ছে
dog1 = Dog("Jack")

# প্রথম Dog-এর নাম প্রিন্ট করা হচ্ছে
print(dog1.name)

# প্রথম Dog-এর Class Variable প্রিন্ট করা হচ্ছে
print(dog1.species)


# দ্বিতীয় Dog Object তৈরি করা হচ্ছে
dog2 = Dog("Rose")

# দ্বিতীয় Dog-এর নাম প্রিন্ট করা হচ্ছে
print(dog2.name)

# দ্বিতীয় Dog-এর Class Variable প্রিন্ট করা হচ্ছে
print(dog2.species)