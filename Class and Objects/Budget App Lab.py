

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = self.name.center(30, '*') + '\n'

        items = ""  
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance()}"

        return title + items + total


def create_spend_chart(categories):

    spent_amounts = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        spent_amounts.append(spent)
    total_spent = sum(spent_amounts)

    percentages = []
    for amount in spent_amounts:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((amount / total_spent) * 100) // 10 * 10)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    
    for i in range(max_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += f"{name[i]}  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"

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