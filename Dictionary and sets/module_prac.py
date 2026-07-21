from math import radians, sin, cos

angle_degress = 40
angle_radians = radians(angle_degress)

sin_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sin_value)
print(cos_value)
# import math	পুরো math মডিউল	math.sqrt()	✅ সবচেয়ে পরিষ্কার ও Best Practice	math. বারবার লিখতে হয়
import math

print(math.sqrt(25))
print(math.pi)

# import math as m পুরো math মডিউল (m নামে) m.sqrt() ✅ ছোট করে লেখা যায় m কী বোঝায়, নতুনদের বুঝতে সময় লাগে
import math as m

print(m.sqrt(25))
print(m.pi)

# from math import sqrt শুধু sqrt sqrt() ✅ math. লিখতে হয় না একাধিক ফাংশন লাগলে আলাদা আলাদা ইমপোর্ট করতে হয়

from math import sqrt

print(sqrt(25))

# সব public ফাংশন sqrt(), sin(), pi ✅ সবচেয়ে কম টাইপ করতে হয় ❌ বড় প্রজেক্টে সমস্যা হতে পারে

from math import *

print(sqrt(25))
print(sin(radians(90)))
print(pi)

