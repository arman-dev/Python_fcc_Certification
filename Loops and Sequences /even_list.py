even_list = []
a = int(input('Enter your limit: '))
for num in range(1,a+1):
    if num%2==0:
        even_list.append(num)
print(even_list)
