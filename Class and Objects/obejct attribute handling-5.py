# UserSession নামে একটি Class তৈরি করা হচ্ছে
class UserSession:

    # Constructor Method
    # Object তৈরি হওয়ার সময় user_id এবং token সেট করবে
    def __init__(self, user_id, token):
        self.user_id = user_id          # User-এর ID সংরক্ষণ করছে
        self.auth_token = token         # Authentication Token সংরক্ষণ করছে
        self.temp_counter = 0           # Temporary Counter সংরক্ষণ করছে


# UserSession Class থেকে একটি Object তৈরি করা হচ্ছে
session = UserSession(101, "a1b2c3d4e5")


# যেসব Attribute Delete করতে হবে তাদের List
attributes_to_clean = ["auth_token", "temp_counter"]


# প্রতিটি Attribute একে একে পরীক্ষা করা হচ্ছে
for attr in attributes_to_clean:

    # hasattr() দিয়ে দেখা হচ্ছে Attribute টি Object-এ আছে কিনা
    if hasattr(session, attr):

        # delattr() ব্যবহার করে Attribute Delete করা হচ্ছে
        delattr(session, attr)

        # কোন Attribute Delete হয়েছে তা প্রিন্ট করা হচ্ছে
        print(f"Removed attribute: {attr}")


# একটি ফাঁকা লাইন দিয়ে Header প্রিন্ট করা হচ্ছে
print("\nFinal attributes remaining:")


# dir() Function Object-এর সকল Attribute এবং Method-এর List Return করে
for attr in dir(session):

    # Special(Magic) Attribute এবং Method বাদ দেওয়া হচ্ছে
    if not attr.startswith("__") and not callable(getattr(session, attr)):

        # বাকি Attribute-এর নাম এবং Value প্রিন্ট করা হচ্ছে
        print(f" - {attr}: {getattr(session, attr)}")


# নিচের Code টি Uncomment করলে dir() এর সবকিছু
# (Magic Methods সহ) প্রিন্ট হবে।
#
# for attr in dir(session):
#     print(f" - {attr}: {getattr(session, attr)}")