import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv") 
print(df.to_string())

line_style = dict(marker = 'o',
                  markersize = 5,
                  markerfacecolor = "red",
                  linestyle = 'solid')

category_quantity = df.groupby("Category")["Quantity"].sum()
print(category_quantity)

plt.plot(category_quantity.index,category_quantity.values,**line_style)
plt.xlabel("category")
plt.ylabel("Total Quanity")
plt.show()