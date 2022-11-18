import pandas as pd
import matplotlib.pyplot as plt


Y1=[1.3,1.2,1.12, 1.08, 1, .94]
X1=[0,20,40,60,80,100]


plt.xlabel("Temperature (C)",fontsize=10)
plt.ylabel("Density (kg/m3)", fontsize= 10)
plt.title("Air Density vs. Temperature")
plt.xlim([0, 100])
plt.ylim([0.8, 1.4])
plt.grid()
point_of_notation_x = [72]
point_of_notation_y= [1.0268]
plt.annotate("72, 1.0268", (72, 1.0268))
plt.plot(X1, Y1, 'bo-', clip_on=False)
plt.plot(point_of_notation_x, point_of_notation_y, 'go-',markersize=10)
plt.show()