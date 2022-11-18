list1=[]
x=1
for x in range(1,6):
    values = int(input(f'Please insert a value for the {x}st integer: '))
    x = x + 1
    list1.append(values)

d= sorted(list1, reverse = True)
a= sorted(list1)
print("Ascending list",a )
print("Descending list",d )