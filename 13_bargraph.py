import matplotlib.pyplot as plt

people = ["Adam", "Eve", "Paul", "Rassel", "Kate", "Peter"]
ages = [45, 25, 67, 70, 21, 34]


xs = range(len(people))
plt.bar(xs, ages)
plt.xticks(xs, people)


plt.ylabel("age")
plt.title("Group of friends")
plt.show()