import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,4,3,9,5,8,4])

y = np.array([33,24,11,90,35,55,25,16])

y1 = np.array([44,14,77,32,75,12,67,27])

plt.title("test scores")

plt.xlabel("hours studied")

plt.ylabel("marks")

plt.scatter(x,y,label = "class A")
plt.scatter(x,y1,label = "class B")

plt.legend()
plt.show()