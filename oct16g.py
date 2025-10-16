# ⿥ PIE CHART: Order Distribution by Category
# ============================================================
# Task: Create a pie chart showing the percentage of total orders for each category.
# Hint:
#   1. Use df['Category'].value_counts() to count orders
#   2. Use plt.pie() with autopct='%1.1f%%' and startangle=90
#   3. Add a title

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")
print(df.to_string())

orders= df['Category'].value_counts()
plt.pie(orders,labels=orders.index,autopct="%1.1f%%",
        startangle=90)

plt.show()
