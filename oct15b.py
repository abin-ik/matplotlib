'''
# Q2: Plot two lines on the same graph — sales of Product A and Product B over 6 months.
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# productA = [120, 150, 170, 190, 210, 230]
# productB = [100, 130, 160, 180, 200, 250]
# - Use different colors and line styles
# - Add a legend


'''

import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
productA = [120,150,170,190,210,230]
productB = [100, 130, 160, 180, 200, 250]


line_style = dict(marker = '<', markersize = 5,
         markerfacecolor = "Yellow",markeredgecolor = 'Black',
         linestyle = "solid",linewidth = 2)

plt.plot(months,productA,color = "#629679",**line_style)
plt.plot(months,productB,color = "Red",**line_style)
plt.legend()
plt.show()
