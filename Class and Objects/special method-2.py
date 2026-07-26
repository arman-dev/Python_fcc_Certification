# Book নামে একটি Class তৈরি করা হচ্ছে
class Book:

    # Constructor Method
    # Object তৈরি হওয়ার সময় title এবং pages সেট করবে
    def __init__(self, title, pages):
        self.title = title      # বইয়ের নাম সংরক্ষণ করছে
        self.pages = pages      # বইয়ের মোট পৃষ্ঠার সংখ্যা সংরক্ষণ করছে

    # Magic Method (__len__)
    # len(object) কল করলে এই Method চালু হবে
    def __len__(self):
        return self.pages

    # Magic Method (__str__)
    # str(object) বা print(object) কল করলে সুন্দরভাবে তথ্য দেখাবে
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages."

    # Magic Method (__eq__)
    # == Operator ব্যবহার করলে এই Method চালু হবে
    # এখানে দুইটি Book-এর Page Number Compare করা হচ্ছে
    def __eq__(self, other):
        return self.pages == other.pages


# প্রথম Book Object তৈরি করা হচ্ছে
book1 = Book("Built wealth like a boss", 230)

# দ্বিতীয় Book Object তৈরি করা হচ্ছে
book2 = Book("War and Peace", 230)


# প্রথম Book-এর মোট Page Number প্রিন্ট করবে (__len__ Method কল হবে)
print(len(book1))

# Book-এর Title (String)-এর মোট Character সংখ্যা প্রিন্ট করবে
print(len(book1.title))

# দ্বিতীয় Book-এর মোট Page Number প্রিন্ট করবে (__len__ Method কল হবে)
print(len(book2))

# প্রথম Book-এর সুন্দর String Representation প্রিন্ট করবে (__str__ Method কল হবে)
print(str(book1))

# pages একটি Integer, তাই এটিকে String-এ রূপান্তর করে প্রিন্ট করবে
print(str(book1.pages))

# দ্বিতীয় Book-এর সুন্দর String Representation প্রিন্ট করবে
print(str(book2))

# দুইটি Book Object-এর Page Number সমান কিনা পরীক্ষা করবে (__eq__ Method কল হবে)
print(book1 == book2)