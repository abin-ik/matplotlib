import matplotlib.pyplot as plt
import numpy as np


x = np.array([34,11,66,22])
fruits = np.array(["apple","banana","ginger","dates"])

plt.pie(x,labels=fruits,autopct="%1.1f%%")
plt.show()