# Book নামে একটি Class তৈরি করা হচ্ছে
class Book:

    # Constructor Method
    # Object তৈরি হওয়ার সময় title এবং page সেট করবে
    def __init__(self, title, page):
        self.title = title      # বইয়ের নাম সংরক্ষণ করছে
        self.page = page        # বইয়ের পৃষ্ঠার সংখ্যা সংরক্ষণ করছে


# প্রথম Book Object তৈরি করা হচ্ছে
obj1 = Book("Red Dragon", 230)

# দ্বিতীয় Book Object তৈরি করা হচ্ছে
obj2 = Book("Anna Careninna", 230)


# Book Object-এর উপর len() ব্যবহার করার চেষ্টা
# Book Class-এ __len__() Method নেই, তাই TypeError হবে
try:
    print(len(obj1))
except:
    print("Ignore")             # Error হলে এই Message প্রিন্ট করবে


# Book-এর Title (String)-এর Length প্রিন্ট করবে
print(len(obj1.title))


# Object-কে String আকারে প্রিন্ট করবে
# __str__() Method না থাকায় Default Object Address দেখাবে
print(str(obj1))


# Page Number-কে String এ রূপান্তর করে প্রিন্ট করবে
print(str(obj1.page))


# দুইটি Object একই কিনা পরীক্ষা করবে
# Defaultভাবে এটি Memory Address Compare করে
print(obj1 == obj2)


# দুইটি Object-এর Page Number Compare করবে
print(obj1.page == obj2.page)