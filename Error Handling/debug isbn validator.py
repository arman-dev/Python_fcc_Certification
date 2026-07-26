# ================= ISBN Validator =================
# print("hi")
def validate_isbn(isbn, length):
    try:
        # ISBN এর দৈর্ঘ্য (Length) সঠিক কিনা পরীক্ষা করা হচ্ছে
        if len(isbn) != length:
            print(f"ISBN-{length} code should be {length} digits long.")
            return

        # শেষ Check Digit বাদ দিয়ে বাকি Digits নেওয়া হচ্ছে
        main_digits = isbn[:length - 1]

        # শেষ Check Digit নেওয়া হচ্ছে (ISBN-10 এর ক্ষেত্রে X হতে পারে)
        given_check_digit = isbn[length - 1].upper()

        # প্রতিটি Digit কে Integer এ রূপান্তর করা হচ্ছে
        # যদি Digit ছাড়া অন্য Character থাকে, তাহলে ValueError হবে
        main_digits_list = [int(digit) for digit in main_digits]

        # ISBN Length অনুযায়ী Expected Check Digit বের করা হচ্ছে
        if length == 10:
            expected_check_digit = calculate_check_digit_10(main_digits_list)
        else:
            expected_check_digit = calculate_check_digit_13(main_digits_list)

        # User এর দেওয়া Check Digit এবং Calculated Check Digit মিলিয়ে দেখা হচ্ছে
        if given_check_digit == expected_check_digit:
            print("Valid ISBN Code.")
        else:
            print("Invalid ISBN Code.")

    # ISBN এর ভিতরে Number ছাড়া অন্য Character থাকলে
    except ValueError:
        print("Invalid character was found.")


# ================= ISBN-10 Check Digit =================

def calculate_check_digit_10(main_digits_list):
    # প্রথম ৯টি Digit ব্যবহার করে Check Digit বের করা হবে

    digits_sum = 0

    # প্রতিটি Digit কে Weight (10 থেকে 2) দিয়ে গুণ করা হচ্ছে
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    # Check Digit হিসাব করা হচ্ছে
    result = 11 - (digits_sum % 11)

    # Result অনুযায়ী Check Digit নির্ধারণ
    if result == 11:
        expected_check_digit = "0"
    elif result == 10:
        expected_check_digit = "X"
    else:
        expected_check_digit = str(result)

    return expected_check_digit


# ================= ISBN-13 Check Digit =================

def calculate_check_digit_13(main_digits_list):
    # প্রথম ১২টি Digit ব্যবহার করে Check Digit বের করা হবে

    digits_sum = 0

    # জোড় Index হলে Weight = 1
    # বিজোড় Index হলে Weight = 3
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    # Check Digit হিসাব করা হচ্ছে
    result = 10 - (digits_sum % 10)

    # Result যদি 10 হয় তাহলে Check Digit হবে 0
    if result == 10:
        expected_check_digit = "0"
    else:
        expected_check_digit = str(result)

    return expected_check_digit


# ================= Main Function =================

def main():
    try:
        # User থেকে ISBN এবং Length ইনপুট নেওয়া হচ্ছে
        # উদাহরণ: 1530051126,10
        user_input = input("Enter ISBN and length: ")

        # কমা দিয়ে দুই ভাগে ভাগ করা হচ্ছে
        values = user_input.split(",")

        # প্রথম অংশ ISBN
        isbn = values[0]

        # দ্বিতীয় অংশ Length (Integer)
        length = int(values[1])

        # Length অবশ্যই 10 অথবা 13 হতে হবে
        if length in (10, 13):
            validate_isbn(isbn, length)
        else:
            print("Length should be 10 or 13.")

    # কমা না দিলে অথবা দ্বিতীয় অংশ না থাকলে
    except IndexError:
        print("Enter comma-separated values.")

    # Length যদি সংখ্যা না হয়
    except ValueError:
        print("Length must be a number.")


# ================= Program Start =================
# FreeCodeCamp Test এর জন্য এটি Comment করে রাখতে হবে

main()