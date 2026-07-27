# MusicalInstrument নামে একটি Class তৈরি করা হচ্ছে
class MusicalInstrument:

    # Constructor Method
    # Object তৈরি হওয়ার সময় Instrument-এর নাম এবং ধরন (Type) সেট করবে
    def __init__(self, name, instrument_type):
        self.name = name                        # Instrument-এর নাম সংরক্ষণ করছে
        self.instrument_type = instrument_type  # Instrument-এর Family/Type সংরক্ষণ করছে

    # Instrument বাজানোর Method
    def play(self):
        # Instrument বাজানোর একটি Message প্রিন্ট করবে
        print(f"The {self.name} is fun to play!")

    # Instrument সম্পর্কে একটি তথ্য Return করবে
    def get_fact(self):
        return f"The {self.name} is part of the {self.instrument_type} family of instruments."


# MusicalInstrument Class থেকে প্রথম Object তৈরি করা হচ্ছে
instrument_1 = MusicalInstrument("Oboe", "woodwind")

# MusicalInstrument Class থেকে দ্বিতীয় Object তৈরি করা হচ্ছে
instrument_2 = MusicalInstrument("Trumpet", "brass")


# প্রথম Instrument-এর নাম প্রিন্ট করতে চাইলে ব্যবহার করা যায়
# print(instrument_1.name)

# প্রথম Instrument-এর Type প্রিন্ট করতে চাইলে ব্যবহার করা যায়
# print(instrument_1.instrument_type)

# দ্বিতীয় Instrument-এর নাম প্রিন্ট করতে চাইলে ব্যবহার করা যায়
# print(instrument_2.name)

# দ্বিতীয় Instrument-এর Type প্রিন্ট করতে চাইলে ব্যবহার করা যায়
# print(instrument_2.instrument_type)


# প্রথম Instrument-এর play() Method কল করা হচ্ছে
instrument_1.play()

# প্রথম Instrument সম্পর্কে তথ্য প্রিন্ট করা হচ্ছে
print(instrument_1.get_fact())


# দ্বিতীয় Instrument-এর play() Method কল করা হচ্ছে
instrument_2.play()

# দ্বিতীয় Instrument সম্পর্কে তথ্য প্রিন্ট করা হচ্ছে
print(instrument_2.get_fact())