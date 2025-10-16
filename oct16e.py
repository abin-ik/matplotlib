# ⿣ LINE GRAPH: Daily Sales Trend
# ============================================================
# Task: Plot a line graph showing total sales per day.
# Hint:
#   1. Convert 'OrderDate' to datetime: df['OrderDate'] = pd.to_datetime(df['OrderDate'])
#   2. Group by 'OrderDate' and sum 'Sales'
#   3. Use plt.plot() with markers and line style
#   4. Label X-axis, Y-axis, and add a title



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")
print(df.to_string())

line_style = dict(marker = "o",
                  markersize =2,
                  markeredgecolor = "red",
                  markerfacecolor = "red",
                  linestyle="solid",
                  color = "green")

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Sales"] = df["Quantity"]*df["Price"]
order_sales = df.groupby("OrderDate")["Sales"].sum()
print(order_sales)
plt.plot(order_sales.index,order_sales.values,**line_style)
plt.tight_layout()
plt.show()