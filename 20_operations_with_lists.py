list1=[]
while True:
    a = float(input("Enter values: "))
    if a >= 0:
        list1.append(a)
    else:
        break

print("Sum:", sum(list1),"Average:", sum(list1)/len(list1),"Max:", max(list1), "Min:", min(list1))








