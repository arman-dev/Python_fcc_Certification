numbers= [num for num in range(1,6)]
result = [(num, 'Even') if num %2 == 0 else (num, 'Odd') for num in numbers]
print(result)