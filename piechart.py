import matplotlib.pyplot as plt
import numpy as np


x = np.array([34,11,66,22])
fruits = np.array(["apple","banana","ginger","dates"])

plt.pie(x,labels=fruits,autopct="%1.1f%%",
        explode=[0,0,0,.3],
        shadow=True,
    
        startangle=180)

plt.title("Fruit sales")
plt.show()