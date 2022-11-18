number = int(input("Number up you want to get the Fibonacci sequence to: "))
x= 0
print(x)
y= 1
print(y)
i = x + y
while (i<=number):
    print(i)
    x = y
    y = i
    i = x + y