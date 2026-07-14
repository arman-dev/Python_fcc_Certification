# secret_num = 3
# my_num = 0
# while my_num!=secret_num:
#     my_num= int(input("Enter Your Guess:"))
#     if my_num!=secret_num:
#         print("Wrong! Try again.")
# print("You got it!")

secret_num = 3
my_num = int(input("Enter Your Guess: "))
while my_num != secret_num:
    print("Wrong! Try again.")
    my_num = int(input("Enter Your Guess: "))
print("You got it!")