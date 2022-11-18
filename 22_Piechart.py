import pandas as pd
import matplotlib.pyplot as plt

movie_type = ["comedy", "action", "romance", "drama", "scifi"]
marks = [4, 5, 6, 1, 4]

plt.pie(marks, labels=movie_type)
plt.legend(title="Favorite type of movie", loc="upper right", bbox_to_anchor=(0,1.05))
plt.show()