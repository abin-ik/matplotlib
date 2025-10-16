# ⿢ BAR GRAPH: Total Sales by Country
# ============================================================
# Task: Create a bar chart showing total sales for each country.
# Hint:
#   1. Add a 'Sales' column: df['Sales'] = df['Quantity'] * df['Price']
#   2. Group by 'Country' and sum 'Sales'
#   3. Sort values in descending order
#   4. Use plt.bar() to plot
#   5. Display the sales value above each bar

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")
print(df.to_string())

df["Sales"] = df["Quantity"]*df["Price"]
quantity_sales = df.groupby("Country")["Sales"].sum().sort_values(ascending=False)
print(quantity_sales)

plt.barh(quantity_sales.index,quantity_sales.values)
plt.show()