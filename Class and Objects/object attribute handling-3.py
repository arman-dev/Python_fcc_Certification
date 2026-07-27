# Configuration নামে একটি খালি Class তৈরি করা হচ্ছে
# বর্তমানে এর ভিতরে কোনো Attribute বা Method নেই
class Configuratin:
    pass


# Dictionary-তে Configuration Settings রাখা হয়েছে
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}


# Configuration Class থেকে একটি Object তৈরি করা হচ্ছে
congig_obj = Configuratin()


# Dictionary-এর প্রতিটি Key এবং Value Loop-এর মাধ্যমে নেওয়া হচ্ছে
for attr_name, attr_value in settings_data.items():

    # attr_name  -> Attribute-এর নাম
    # attr_value -> Attribute-এর মান

    # print(attr_name, attr_value)

    # setattr() ব্যবহার করে Object-এর মধ্যে নতুন Attribute তৈরি করা হচ্ছে
    # উদাহরণ:
    # congig_obj.server_url = "https://api.example.com"
    # congig_obj.timeout_sec = 30
    # congig_obj.max_retries = 5
    setattr(congig_obj, attr_name, attr_value)


# Object-এর server_url Attribute প্রিন্ট করবে
print(congig_obj.server_url)

# Object-এর timeout_sec Attribute প্রিন্ট করবে
print(congig_obj.timeout_sec)

# print(congig_obj.30)
# ❌ এটি ভুল (SyntaxError)
# কারণ Attribute-এর নাম সংখ্যা (30) হতে পারে না।
# Python-এ Dot Notation-এর পরে অবশ্যই একটি বৈধ Identifier থাকতে হবে।

# print(congig_obj.attr_name)
# ❌ এটি server_url প্রিন্ট করবে না।
# কারণ Object-এ attr_name নামে কোনো Attribute তৈরি হয়নি।
# Loop Variable-এর নাম attr_name ছিল, কিন্তু Object-এর Attribute-এর নাম
# server_url, timeout_sec এবং max_retries।

# Dynamic Attribute Access করতে চাইলে getattr() ব্যবহার করতে হবে।