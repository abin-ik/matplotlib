
# Sample Dataset ⿢: Age vs Annual Income by Gender

# ⿢ Plot a scatter graph comparing 'Age' and 'Annual Income' from the dataset.
#     - Use different colors or markers for different 'Gender' categories.




import pandas as pd
import matplotlib.pyplot as plt 


df_income = pd.DataFrame({
    'Age': [22, 25, 27, 29, 30, 32, 35, 37, 40, 45],
    'Annual Income': [25000, 27000, 30000, 33000, 36000, 40000, 45000, 48000, 52000, 60000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})

ckk= df_income["Gender"].map({'Male':"blue","Female" : "green"})
plt.scatter(df_income["Age"],df_income["Annual Income"],c = ckk)

import pandas as pd
import matplotlib.pyplot as plt 


df_income = pd.DataFrame({
    'Age': [22, 25, 27, 29, 30, 32, 35, 37, 40, 45],
    'Annual Income': [25000, 27000, 30000, 33000, 36000, 40000, 45000, 48000, 52000, 60000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})

ckk= df_income["Gender"].map({'Male':"blue","Female" : "green"})
plt.scatter(df_income["Age"],df_income["Annual Income"],c = ckk)
plt.scatter([], [], c='blue', label='Male')
plt.scatter([], [], c='green', label='Female')

plt.legend()


plt.legend()
plt.show()