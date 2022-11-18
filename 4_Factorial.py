result = int(input("Insert a factorial number you want to compute: "))
for i in range((result-1),1,-1):
    result = result * i

print("the sum of natural numbers is: ", result)