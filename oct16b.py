import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv") 
print(df.to_string())

category_quantity = df.groupby("Category")["Quantity"].sum()
print(category_quantity)

plt.bar(category_quantity.index,category_quantity.values)
plt.show()