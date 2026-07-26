# Car নামে একটি Class তৈরি করা হচ্ছে
class Car:

    # Constructor Method
    # Object তৈরি হওয়ার সময় color এবং model সেট করবে
    def __init__(self, color, model):
        self.color = color      # Car-এর রঙ সংরক্ষণ করছে
        self.model = model      # Car-এর Model সংরক্ষণ করছে

    # Car-এর তথ্য Return করার Method
    def description(self):
        return f"Color: {self.color}, Model: {self.model}"


# প্রথম Car Object তৈরি করা হচ্ছে
obj1 = Car("Red", "BMW")

# দ্বিতীয় Car Object তৈরি করা হচ্ছে
obj2 = Car("Black", "Toyota")


# প্রথম Car-এর Color প্রিন্ট করা হচ্ছে
print(obj1.color)

# প্রথম Car-এর Model প্রিন্ট করা হচ্ছে
print(obj1.model)

# প্রথম Car-এর Description Method কল করা হচ্ছে
print(obj1.description())


# দ্বিতীয় Car-এর Color প্রিন্ট করা হচ্ছে
print(obj2.color)

# দ্বিতীয় Car-এর Model প্রিন্ট করা হচ্ছে
print(obj2.model)

# দ্বিতীয় Car-এর Description Method কল করা হচ্ছে
print(obj2.description())