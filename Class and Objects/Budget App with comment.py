# Category নামে একটি Class তৈরি করা হচ্ছে
# এই Class ব্যবহার করে বিভিন্ন বাজেট ক্যাটাগরি (যেমন Food, Clothing, Entertainment)
# তৈরি করা যাবে।
class Category:

    # Constructor Method (__init__)
    # যখন নতুন Object তৈরি হবে, তখন এই Method স্বয়ংক্রিয়ভাবে কল হবে।
    # name প্যারামিটারটি Category-এর নাম গ্রহণ করবে।
    def __init__(self, name):

        # Category-এর নাম Object-এর ভিতরে সংরক্ষণ করা হচ্ছে।
        # উদাহরণ:
        # Category("Food") --> self.name = "Food"
        self.name = name

        # ledger নামে একটি খালি List তৈরি করা হচ্ছে।
        # এই List-এর ভিতরে Category-এর সকল Transaction সংরক্ষণ হবে।
        # প্রতিটি Transaction একটি Dictionary হবে।
        # উদাহরণ:
        # {
        #     "amount": 500,
        #     "description": "Salary"
        # }
        # অথবা
        # {
        #     "amount": -200,
        #     "description": "Lunch"
        # }
        # শুরুতে কোনো Transaction নেই,
        # তাই List খালি রাখা হয়েছে।
        self.ledger = []

    # ===========================
    # Deposit Method
    # ===========================
    # এই Method Category-তে টাকা যোগ (Deposit) করার জন্য ব্যবহৃত হবে।
    # amount = কত টাকা জমা হবে
    # description = ঐ Transaction-এর বর্ণনা
    # description="" দেওয়ার অর্থ, User যদি Description না দেয়,
    # তাহলে Default হিসেবে Empty String ব্যবহার হবে।
    # উদাহরণ:
    # food.deposit(1000)
    # অথবা
    # food.deposit(1000, "Salary")
    def deposit(self, amount, description=""):
        # append() Method List-এর শেষে নতুন Item যোগ করে।
        # এখানে List-এর মধ্যে একটি Dictionary যোগ করা হচ্ছে।
        # Dictionary-তে দুটি Key থাকবে:
        # amount
        # description
        # উদাহরণ:
        # food.deposit(1000, "Salary")
        # ledger হবে:
        # [
        #     {
        #         "amount": 1000,
        #         "description": "Salary"
        #     }
        # ]
        self.ledger.append({

            # জমা হওয়া টাকার পরিমাণ
            'amount': amount,

            # Transaction-এর Description
            'description': description
        })

    # ===========================
    # Get Balance Method
    # ===========================
    # এই Method Category-এর বর্তমান Balance বের করবে।
    # Balance = Deposit - Withdraw
    # যেহেতু Withdraw Negative Amount হিসেবে Store হয়,
    # তাই শুধু সব Amount যোগ করলেই Final Balance পাওয়া যাবে।
    def get_balance(self):
        # total নামে একটি Variable তৈরি করা হচ্ছে।
        # শুরুতে Balance = 0
        total = 0
        # ledger List-এর প্রতিটি Transaction-এর উপর Loop চলছে।
        # ধরুন:
        # ledger =
        # [
        #     {"amount": 1000, "description": "Salary"},
        #     {"amount": -200, "description": "Lunch"},
        #     {"amount": 300, "description": "Gift"}
        # ]
        # তাহলে Loop ৩ বার চলবে।
        for item in self.ledger:
            # প্রতিটি Dictionary-এর amount Key-এর Value নেওয়া হচ্ছে।
            # প্রথমবার:
            # total = 0 + 1000
            # দ্বিতীয়বার:
            # total = 1000 + (-200)
            # তৃতীয়বার:
            # total = 800 + 300
            total += item['amount']

        # সব Transaction যোগ করার পরে
        # Final Balance Return করা হচ্ছে।
        # উপরের উদাহরণে Return হবে:
        # 1100
        return total

    # ===========================
    # Check Funds Method
    # ===========================
    # এই Method-এর কাজ হলো,
    # Withdraw বা Transfer করার আগে পর্যাপ্ত Balance আছে কিনা পরীক্ষা করা।
    # Return করবে:
    # True  -> যদি যথেষ্ট টাকা থাকে
    # False -> যদি যথেষ্ট টাকা না থাকে
    def check_funds(self, amount):
        # বর্তমান Balance বের করা হচ্ছে।
        # self.get_balance() Method পুরো Ledger হিসাব করে Balance Return করে।
        # উদাহরণ:
        # Current Balance = 500
        # Withdraw করতে চাই = 700
        # তাহলে
        # 700 > 500
        # অর্থাৎ টাকা যথেষ্ট নেই।
        if amount > self.get_balance():

            # পর্যাপ্ত টাকা না থাকলে False Return করবে।
            return False
        # যদি উপরের Condition False হয়,
        # অর্থাৎ Balance যথেষ্ট থাকে,
        # তাহলে True Return করবে।
        return True

    # ===========================
    # Withdraw Method
    # ===========================
    # এই Method Category থেকে টাকা কাটার জন্য ব্যবহৃত হয়।
    # amount = কত টাকা Withdraw হবে
    # description = ঐ Transaction-এর Description
    def withdraw(self, amount, description=""):
        # Withdraw করার আগে Balance পরীক্ষা করা হচ্ছে।
        # check_funds() যদি True Return করে,
        # তাহলে Withdraw করা যাবে।
        if self.check_funds(amount):
            # Withdraw Ledger-এ Negative Amount হিসেবে Store করা হয়।
            # উদাহরণ:
            # Withdraw = 200
            # Store হবে:
            # {
            #     "amount": -200,
            #     "description": "Lunch"
            # }
            self.ledger.append({
                # Negative Amount Store করা হচ্ছে।
                'amount': -amount,
                # Withdraw-এর Description
                'description': description
            })
            # সফলভাবে Withdraw হলে True Return করবে।
            return True

        # যদি Balance পর্যাপ্ত না থাকে,
        # তাহলে কিছুই Store হবে না।
        # False Return করবে।
        return False

    # ===========================
    # Transfer Method
    # ===========================
    # এই Method এক Category থেকে অন্য Category-তে
    # টাকা Transfer করার জন্য ব্যবহৃত হয়।
    # amount = কত টাকা Transfer হবে
    # category_instance =
    # যে Category-তে টাকা যাবে।
    # উদাহরণ:
    # food.transfer(100, clothing)
    # Food থেকে 100 টাকা Clothing-এ যাবে।
    def transfer(self, amount, category_instance):
        # প্রথমে পরীক্ষা করা হচ্ছে,
        # পর্যাপ্ত Balance আছে কিনা।
        if self.check_funds(amount):
            # বর্তমান Category থেকে টাকা Withdraw করা হচ্ছে।
            # Description হবে:
            # Transfer to Clothing
            self.withdraw(
                amount,
                f"Transfer to {category_instance.name}"
            )
            # অন্য Category-তে একই Amount Deposit করা হচ্ছে।
            # Description হবে:
            # Transfer from Food
            category_instance.deposit(
                amount,
                f"Transfer from {self.name}"
            )
            # সফলভাবে Transfer সম্পন্ন হলে
            # True Return করবে।
            return True
        
        # Balance যথেষ্ট না থাকলে
        # কোনো Transfer হবে না।
        # False Return করবে।
        return False

    # ===========================
    # Magic Method (__str__)
    # ===========================
    # এই Method-এর কাজ হলো Object-কে সুন্দরভাবে String আকারে দেখানো।
    # যখন আমরা লিখি:
    # print(food)
    # তখন Python স্বয়ংক্রিয়ভাবে:
    # food.__str__() কল করে।
    # যদি এই Method না লিখি,
    # তাহলে Output হবে এরকম:
    # <__main__.Category object at 0x7f4c9b1f2d60>
    # যা User-এর জন্য বোঝা কঠিন।
    # তাই __str__() Method ব্যবহার করে সুন্দর Output তৈরি করা হচ্ছে।
    def __str__(self):

        # ===============================
        # Title তৈরি করা হচ্ছে
        # ===============================
        # center(width, fillchar)
        # width = মোট কত Character হবে
        # fillchar = কোন Character দিয়ে ফাঁকা জায়গা পূরণ হবে
        # উদাহরণ:
        # self.name = "Food"
        # তাহলে
        # "Food".center(30, "*")
        # Result:
        # *************Food*************
        title = self.name.center(30, "*") + "\n"

        # ===============================
        # Ledger-এর সব Transaction রাখার জন্য
        # একটি Empty String তৈরি করা হচ্ছে।
        # ===============================
        items = ""

        # ===============================
        # Ledger-এর প্রতিটি Transaction-এর উপর Loop চলছে।
        # ===============================
        # উদাহরণ:
        # [
        #   {"amount": 1000, "description":"Salary"},
        #   {"amount": -200, "description":"Lunch"}
        # ]
        for item in self.ledger:

            # ======================================
            # Description Formatting
            # ======================================
            # item["description"][:23]
            # Description যদি 23 Character-এর বেশি হয়,
            # তাহলে প্রথম 23 Character নেওয়া হবে।
            # উদাহরণ:
            # "Bought vegetables from supermarket"
            # হবে
            # "Bought vegetables fro"
            # :<23
            # Left Alignment
            # অর্থাৎ Description বাম পাশে থাকবে,
            # আর মোট 23 Character জায়গা দখল করবে।
            desc = f"{item['description'][:23]:<23}"

            # ======================================
            # Amount Formatting
            # ======================================
            # >7.2f
            # >
            # = Right Align
            # 7
            # = মোট 7 Character জায়গা নেবে
            # .2f
            # = Decimal-এর পরে 2 Digit দেখাবে
            # উদাহরণ:
            # 25
            # হবে
            # "  25.00"
            amt = f"{item['amount']:>7.2f}"

            # ======================================
            # Description + Amount
            # এক লাইনে যোগ করা হচ্ছে।
            # ======================================
            # উদাহরণ:
            # Salary                 1000.00
            items += f"{desc}{amt}\n"

        # ======================================
        # শেষে Total Balance তৈরি করা হচ্ছে।
        # ======================================
        # get_balance() Method Call করে
        # Current Balance বের করা হচ্ছে।
        total = f"Total: {self.get_balance()}"

        # ======================================
        # সবকিছু একসাথে Return করা হচ্ছে।
        # ======================================
        # Title
        # +
        # সব Transaction
        # +
        # Total Balance
        return title + items + total

# ==================================================
# Function: create_spend_chart()
# ==================================================
# এই Function-এর কাজ হলো বিভিন্ন Category-এর
# Spending Percentage হিসাব করে একটি Vertical Chart তৈরি করা
# উদাহরণ:
# Food --------> 50%
# Clothing ----> 30%
# Auto --------> 20%
# Output হবে:
# Percentage spent by category
# 100|
#  90|
#  80|
#  ...
#
def create_spend_chart(categories):

    # =====================================
    # প্রতিটি Category কত টাকা খরচ করেছে
    # তা রাখার জন্য একটি Empty List।
    # =====================================
    spent_amounts = []

    # =====================================
    # প্রতিটি Category-এর উপর Loop চলছে।
    # =====================================
    # categories =
    # [food, clothing, auto]
    #
    for category in categories:

        # এই Category কত টাকা Spend করেছে
        # তা রাখার জন্য Variable।
        spent = 0

        # =====================================
        # Ledger-এর প্রতিটি Transaction দেখা হচ্ছে।
        # =====================================
        for item in category.ledger:
            # Withdraw সবসময় Negative Amount।
            # Deposit Positive।
            # তাই শুধু Negative Amount গুলোই
            # Spending হিসেবে ধরা হবে।
            if item['amount'] < 0:

                # abs()
                # Absolute Value Return করে।
                # -200
                # হবে
                # 200
                spent += abs(item['amount'])

        # এই Category-এর মোট Spending List-এ যোগ করা হচ্ছে।
        spent_amounts.append(spent)

    # =====================================
    # সব Category মিলিয়ে মোট Spending বের করা হচ্ছে।
    # =====================================
    total_spent = sum(spent_amounts)

    # =====================================
    # Percentage রাখার জন্য Empty List।
    # =====================================
    percentages = []

    # =====================================
    # প্রতিটি Category-এর Spending Percentage
    # হিসাব করা হচ্ছে।
    # =====================================
    for amount in spent_amounts:

        # যদি কোনো Spending না থাকে
        # তাহলে Percentage = 0
        if total_spent == 0:
            percentages.append(0)

        else:
            # =====================================
            # Percentage Formula
            # (Category Spending / Total Spending)
            # ×100
            # তারপর নিচের 10-এর ঘরে নামিয়ে আনা হচ্ছে।
            # উদাহরণ:
            # 56%
            # হবে
            # 50%
            #
            # 84%
            # হবে
            # 80%
            #
            # কারণ Chart প্রতি 10% Interval ব্যবহার করে।
            # =====================================
            percentages.append(
                int((amount / total_spent) * 100) // 10 * 10
            )

    # =====================================
    # Chart-এর প্রথম Heading তৈরি করা হচ্ছে।
    # =====================================
    chart = "Percentage spent by category\n"

    # =====================================
    # Y-axis তৈরি করা হচ্ছে।
    #
    # range(100, -1, -10)
    #
    # Output:
    #
    # 100
    # 90
    # 80
    # ...
    # 0
    # =====================================
    for i in range(100, -1, -10):

        # সংখ্যা Right Align করে যোগ করা হচ্ছে।
        #
        # উদাহরণ:
        #
        # 100|
        #
        #  90|
        #
        chart += f"{i:>3}| "

        # প্রতিটি Category-এর Percentage দেখা হচ্ছে।
        for percent in percentages:

            # যদি ঐ Category-এর Percentage
            # বর্তমান Line-এর সমান বা বেশি হয়
            if percent >= i:

                # তাহলে "o" বসবে।
                chart += "o  "

            else:

                # না হলে ফাঁকা থাকবে।
                chart += "   "

        # প্রতিটি Row শেষে New Line।
        chart += "\n"


    # =====================================
    # X-axis তৈরি করা হচ্ছে।
    #
    # Category যতটি,
    # সেই অনুযায়ী Dash তৈরি হবে।
    # =====================================
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"


    # =====================================
    # সব Category-এর নাম List-এ নেওয়া হচ্ছে।
    # =====================================
    #
    # উদাহরণ:
    #
    # ["Food","Clothing","Auto"]
    #
    names = [category.name for category in categories]


    # =====================================
    # সবচেয়ে বড় নামের Length বের করা হচ্ছে।
    #
    # উদাহরণ:
    #
    # Food = 4
    # Clothing = 8
    # Auto = 4
    #
    # max_length = 8
    # =====================================
    max_length = max(len(name) for name in names)


    # =====================================
    # এখন Vertical ভাবে নাম প্রিন্ট করা হবে।
    # =====================================
    #
    # i = 0
    #
    # F C A
    #
    # i = 1
    #
    # o l u
    #
    # i = 2
    #
    # o o t
    #
    for i in range(max_length):

        # বাম পাশে ৫টি Space।
        chart += "     "

        # প্রতিটি Category-এর নাম দেখা হচ্ছে।
        for name in names:

            # যদি ঐ Position-এ Character থাকে
            if i < len(name):

                # Character যোগ করা হচ্ছে।
                chart += f"{name[i]}  "

            else:

                # না থাকলে ফাঁকা Space।
                chart += "   "

        # শেষ Line ছাড়া
        # প্রতিটি Line শেষে New Line।
        if i < max_length - 1:
            chart += "\n"


    # =====================================
    # সম্পূর্ণ Chart Return করা হচ্ছে।
    # =====================================
    return chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
food.transfer(50, clothing)

clothing.deposit(500, "initial deposit")
clothing.withdraw(25.50, "t-shirt")

print(food)
print("\n")
print(create_spend_chart([food, clothing, auto]))