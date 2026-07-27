# Planet নামে একটি Class তৈরি করা হচ্ছে
class Planet:

    # Constructor Method
    # Object তৈরি হওয়ার সময় name, planet_type এবং star সেট করবে
    def __init__(self, name, planet_type, star):

        # তিনটি Argument-ই String কিনা পরীক্ষা করা হচ্ছে
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet_type, and star must be strings")

        # কোনো String খালি (Empty) কিনা পরীক্ষা করা হচ্ছে
        if not name or not planet_type or not star:
            raise ValueError("name, planet_type, and star must be non-empty strings")

        # Instance Variables-এ মান সংরক্ষণ করা হচ্ছে
        self.name = name
        self.planet_type = planet_type
        self.star = star

    # Planet কোন Star-এর চারপাশে ঘুরছে তা Return করবে
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    # Magic Method (__str__)
    # print(object) বা str(object) কল করলে সুন্দরভাবে তথ্য দেখাবে
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# Planet Class থেকে প্রথম Object তৈরি করা হচ্ছে
planet_1 = Planet("Earth", "Terrestrial", "Sun")

# দ্বিতীয় Planet Object তৈরি করা হচ্ছে
planet_2 = Planet("Pluto", "Gas Giant", "Sun")

# তৃতীয় Planet Object তৈরি করা হচ্ছে
planet_3 = Planet("Mars", "Terrestrial", "Sun")


# প্রতিটি Planet-এর তথ্য (__str__ Method) প্রিন্ট করা হচ্ছে
print(planet_1)
print(planet_2)
print(planet_3)


# প্রতিটি Planet-এর orbit() Method কল করে Message প্রিন্ট করা হচ্ছে
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())


# নিচেরগুলোও একই কাজ করবে,
# তবে Return Value দেখাতে print() ব্যবহার করতে হবে।
# planet_2.orbit()
# planet_3.orbit()