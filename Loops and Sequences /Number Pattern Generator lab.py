def number_pattern(n):
    if not isinstance (n, int):
        return "Argument must be an integer value."
    elif n<1:
        return "Argument must be an integer greater than 0."
    else:
        sum = ""
        for i in range(1, n+1):
            sum +=str(i)+ " "
    return sum.strip()
print(number_pattern(4))