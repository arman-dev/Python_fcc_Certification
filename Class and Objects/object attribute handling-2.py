# Person নামে একটি Class তৈরি করা হচ্ছে
class Person:

    # Constructor Method
    # নতুন Object তৈরি হওয়ার সময় name এবং age সেট করবে
    def __init__(self, name, age):
        self.name = name      # Instance Variable: Person-এর নাম সংরক্ষণ করছে
        self.age = age        # Instance Variable: Person-এর বয়স সংরক্ষণ করছে


# Person Class থেকে একটি Object তৈরি করা হচ্ছে
person1 = Person("Arman", 27)


# dir() Function Object-এর সকল Attribute এবং Method-এর একটি List Return করে
# যেমন: __class__, __init__, __str__, name, age ইত্যাদি
for attr in dir(person1):

    # __ দিয়ে শুরু হওয়া Special/Magic Attribute বাদ দেওয়া হচ্ছে
    # যেমন: __class__, __dict__, __module__ ইত্যাদি
    #
    # callable() Function পরীক্ষা করে Attribute টি Function/Method কিনা
    # যদি Method হয় তাহলে True Return করবে
    #
    # এখানে Method গুলোও বাদ দেওয়া হচ্ছে
    # ফলে শুধুমাত্র Data Attribute (name, age) পাওয়া যাবে
    if not attr.startswith("__") and not callable(getattr(person1, attr)):

        # getattr() ব্যবহার করে বর্তমান Attribute-এর Value নেওয়া হচ্ছে
        value = getattr(person1, attr)

        # Attribute-এর নাম এবং Value প্রিন্ট করা হচ্ছে
        print(f"{attr}: {value}")