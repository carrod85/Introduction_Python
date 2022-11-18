
x = int(input("Please insert a number you want to get the factorials of: "))
y = x
z = 1
while y >= 1:
    if x % y == 0:
        print("number ", z, ": ", y)
        z = z + 1
    y = y - 1
