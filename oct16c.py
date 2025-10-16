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

plt.pie(category_quantity.values,labels =category_quantity.index,
        autopct="%1.1f%%",
        explode=[0.5,0,0],
        shadow=True,
        startangle=180)
plt.show()