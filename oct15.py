'''# ⿡ LINE GRAPH
# ------------------------------------------------------------
# Q1: Create a line graph to show the population growth of India from 2000 to 2020.
# years = [2000, 2005, 2010, 2015, 2020]
# population = [1.0, 1.1, 1.2, 1.3, 1.38]
# - Add labels for x and y axes
# - Add title "Population Growth of India (2000–2020)"
# - Display grid lines

'''
import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2005, 2010, 2015, 2020])
population = np.array([1.0, 1.1, 1.2, 1.3, 1.38])
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

plt.plot(years,population)
plt.xlabel("years")
plt.ylabel("population")
plt.title("opulation Growth of India (2000–2020)")
plt.grid(linewidth = .5, color = "#87f07f" ,linestyle ="-.")
plt.show()
