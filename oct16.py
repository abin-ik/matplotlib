import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])

figure , axes = plt.subplots(2,2)

axes[0,0].plot(x,x*2,color = "blue")
axes[0,0].set_title("x*2")

axes[0,1].plot(x,x**2,color = "yellow")
axes[0,1].set_title("x**2")

axes[1,0].plot(x,x**3,color ="green")
axes[1,0].set_title("x*3")

axes[1,1].plot(x,x**3,color = "red")
axes[1,1].set_title("x**3")

plt.tight_layout()
plt.show()