# ⿦ PIE CHART: Country-wise Share of Total Sales
# ============================================================
# Task: Plot a pie chart showing the share of total sales by country.
# Hint:
#   1. Group by 'Country' and sum 'Sales'
#   2. Use plt.pie() with labels, autopct='%1.1f%%', colors, and shadow=True
#   3. Add a title

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")
print(df.to_string())

df["Sales"] = df["Quantity"]*df["Price"]
country_sales = df.groupby("Country")["Sales"].sum()
print(country_sales)

plt.figure(figsize=(100,100))

plt.pie(country_sales,labels=country_sales.index,
        autopct="%1.1f%%",startangle=90,
        shadow=True)
plt.tight_layout()
plt.show()