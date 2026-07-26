# ============ 1. raise ValueError Example =============

# def check_age(age):
#     if age < 0:                                   # বয়স ০-এর কম হলে
#         raise ValueError("Age cannot be Negative") # নিজে থেকে ValueError তৈরি করবে
#     return age                                    # বৈধ বয়স হলে return করবে

# try:
#     print(check_age(7))                           # ফাংশন কল করা হচ্ছে
# except ValueError as e:
#     print(f"Error Occurred: {e}")                 # Error হলে মেসেজ প্রিন্ট করবে


# ============ 2. Re-raise Exception Example =============

# def process_data(data):
#     try:
#         result = int(data)                        # String কে integer এ রূপান্তরের চেষ্টা
#         return result * 2                         # সফল হলে ২ দিয়ে গুণ করবে
#     except:
#         print("Logging invalid data received.")   # Error লগ করবে
#         raise                                    # একই Error আবার উপরের level-এ পাঠাবে

# try:
#     print(process_data("Hello"))                  # "Hello" int হবে না
# except ValueError:
#     print("Handled at Higher Level.")             # উপরের level-এ Error handle করবে


# ============ 3. Custom Exception Example =============

# class InsufficientFundsError(Exception):          # নিজের Exception Class তৈরি
#     def __init__(self, balance, amount):
#         self.balance = balance                    # বর্তমান Balance সংরক্ষণ
#         self.amount = amount                      # Withdraw Amount সংরক্ষণ
#         super().__init__(
#             f"Insufficient Funds: ${balance} available, ${amount} requested."
#         )                                         # Parent Exception-এ Message পাঠানো

# def withdraw(balance, amount):
#     if balance < amount:                          # Balance কম হলে
#         raise InsufficientFundsError(balance, amount)  # Custom Exception Raise করবে
#     return balance - amount                       # না হলে নতুন Balance Return করবে

# try:
#     print(withdraw(1200, 123))
# except InsufficientFundsError as e:
#     print(f"Transaction Failed: {e}")             # Error Message প্রিন্ট করবে


# ============ 4. Raising Exception with 'from' =============

# def parse_config(filename):
#     try:
#         with open(filename, 'r') as file:         # File Open করা হচ্ছে
#             data = file.read()                    # File থেকে Data পড়া হচ্ছে
#             return int(data)                      # Data কে Integer এ রূপান্তর
#
#     except FileNotFoundError:
#         raise ValueError("Configuration file is missing") from None
#         # আসল FileNotFoundError লুকিয়ে নতুন ValueError দেখাবে
#
#     except ValueError as e:
#         raise ValueError("Invalid configuration format") from e
#         # আগের ValueError এর কারণসহ নতুন ValueError Raise করবে

# config = parse_config("config.txt")


# ============ 5. assert Statement Example =============

def calculate_square_root(number):
    # সংখ্যা ০ বা তার বেশি কিনা পরীক্ষা করবে
    assert number >= 0, "Cannot calculate square of a negative number."

    # শর্ত সত্য হলে Square Root Return করবে
    return number ** 0.5

try:
    # Negative Number পাঠানো হয়েছে
    result = calculate_square_root(-4)

except AssertionError as e:
    # Assertion ব্যর্থ হলে Error Message প্রিন্ট করবে
    print(f"Assertion failed: {e}")