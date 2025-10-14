import matplotlib.pyplot as plt
import numpy as np

fruits = np.array(['apples','banans','cherry','Blue berry'])

sales = np.array([400,250,100,500])

line_style = dict(fontsize = 13, color = "green")

plt.bar(fruits,sales,color = "skyblue")

plt.title("fruit size " ,fontsize = 14)
plt.xlabel("fruits",**line_style)
plt.ylabel("sales",**line_style)

plt.show()