# ======== 1. try-except-else-finally Example ========

# try:
#     a = 10 / 0                     # Zero দিয়ে ভাগ করার চেষ্টা (Error হবে)
#     print(a)                       # Error না হলে a প্রিন্ট করবে
# except:
#     print("You can't Divide by Zero.")   # Error হলে এই ব্লক চলবে
# else:
#     print("Division Successful", a)      # Error না হলে এই ব্লক চলবে
# finally:
#     print("This block always runs")      # Error হোক বা না হোক, সবসময় চলবে


# ======== 2. Multiple Exception Handling ========

# try:
#     a = int("rahim")              # String কে int এ রূপান্তর করতে গিয়ে ValueError হবে
#     b = 13
#     output = a / b                # আগের লাইনে Error হওয়ায় এটি চলবে না
# except ZeroDivisionError:
#     print("You can't Divide by Zero")    # ZeroDivisionError হলে চলবে
# except ValueError:
#     print("This is not a valid Number.") # ValueError হলে চলবে


# ======== 3. Exception Object ========

# try:
#     a = 12 / 0                    # Zero দিয়ে ভাগ করলে ZeroDivisionError হবে
# except ZeroDivisionError as e:
#     print(f"Error occurred: {e}") # Error message e ভেরিয়েবলে সংরক্ষণ করে প্রিন্ট করবে


# ======== 4. Handling Multiple Exceptions Together ========

try:
    a = int(input("Enter a Value: "))      # User থেকে একটি সংখ্যা ইনপুট নেওয়া হচ্ছে
    result = 10 / a                        # 10 কে ইনপুটকৃত সংখ্যা দিয়ে ভাগ করা হচ্ছে
    print(result)                          # ফলাফল প্রিন্ট করবে

except (ZeroDivisionError, ValueError) as e:
    # ZeroDivisionError বা ValueError যেকোনো একটি হলে এই ব্লক চলবে
    print(f"Error Occurred: {e}")          # আসল Error message প্রিন্ট করবে