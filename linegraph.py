import matplotlib.pyplot as plt
import numpy as np

x = np.array([2022,2023,2024,2025])
y = np.array([0,0,23,25])
y1 = np.array([10,30,43,25])

line_style = dict(marker = '<', markersize = 5,
         markerfacecolor = "Yellow",markeredgecolor = 'Black',
         linestyle = "solid",linewidth = 2)

plt.plot(x,y,color = "#629679",**line_style)
plt.plot(x,y1,color = "Red",**line_style)



plt.title("Line Graph", fontsize = 15, family = "cursive" , fontweight = "bold" , color = "orange")
styles = dict (fontsize = 10, family = "manospace" , fontweight = "semibold" , color = "#6027f2")

plt.xlabel("years" ,**styles)

plt.ylabel("students ", **styles)

plt.grid(linewidth = .5, color = "#87f07f" ,linestyle ="-.")

plt.tick_params(axis="both", colors = "green")

plt.xticks(x)

plt.show()
