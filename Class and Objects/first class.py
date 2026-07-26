# Dog নামে একটি Class তৈরি করা হচ্ছে
class Dog:

    # Constructor Method
    # Object তৈরি হওয়ার সময় name এবং age সেট করবে
    def __init__(self, name, age):
        self.name = name      # Dog-এর নাম সংরক্ষণ করছে
        self.age = age        # Dog-এর বয়স সংরক্ষণ করছে

    # Dog-এর Bark করার Method
    def bark(self):
        # Dog-এর নাম Uppercase করে এবং বয়সসহ Message প্রিন্ট করবে
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old.")


# Dog Class থেকে প্রথম Object তৈরি করা হচ্ছে
dog_1 = Dog("Jack", 56)

# Dog Class থেকে দ্বিতীয় Object তৈরি করা হচ্ছে
dog_2 = Dog("Github", 6)


# প্রথম Dog-এর bark() Method কল করা হচ্ছে
dog_1.bark()

# দ্বিতীয় Dog-এর bark() Method কল করা হচ্ছে
dog_2.bark()