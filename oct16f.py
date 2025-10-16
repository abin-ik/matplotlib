# ============================================================
# ⿤ LINE GRAPH: Category-wise Average Price
# ============================================================
# Task: Draw a line chart showing the average product price per category.
# Hint:
#   1. Group by 'Category' and calculate mean of 'Price'
#   2. Use plt.plot() with markers, colors, and line style
#   3. Label axes and add grid lines

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")
print(df.to_string())

average_product = df.groupby("Category")['Price'].mean()
print(average_product)

line_style = dict(marker = "o",
                  markersize =2,
                  markeredgecolor = "red",
                  markerfacecolor = "red",
                  linestyle="solid",
                  color = "green")

plt.xlabel("category")
plt.ylabel("mean price")

plt.grid(color = "yellow")

plt.plot(average_product.index,average_product.values,**line_style)

plt.show()