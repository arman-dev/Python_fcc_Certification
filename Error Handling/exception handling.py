# ========11111111111111111111111==============


# try:
#     a = 10/0
#     print(a)
# except:
#     print("You can't Divide by Zero.")
# else:
#     print("Division Successfull", a)
# finally:
#     print("This block always run")


# ==========222222222222222222222============


# try:
#     a = int("rahim")
#     b = 13
#     output = a/b
# except ZeroDivisionError:
#     print("You can't Divide by Zero")
# except ValueError:
#     print("This is not a valid Number.")


# ==========33333333333333333333333=============

# try:
#     a = 12/0
# except ZeroDivisionError as e:
#     print(f"Error occurred:{e}")


# ============4444444444444444444==========
try:
    a = int(input("Enter a Value:"))
    result = 10/a
    print(result)
except (ZeroDivisionError,ValueError) as e:
    print(f"Error Occurred:{e}")