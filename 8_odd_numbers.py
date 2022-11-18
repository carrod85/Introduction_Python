number = int(input("input the integer you want to know the odd numbers up to: "))

for i in range (number, 0, -1):
    if i % 2 != 0:
        print(i)
