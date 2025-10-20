import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score


df = pd.read_csv("salaries.csv")
#print(df.to_string())

#print(df.isnull().sum())

#work_year,experience_level,employment_type,job_title,salary,salary_currency,
# salary_in_usd,employee_residence,remote_ratio,company_location,company_size

x = df[['work_year','experience_level','employment_type','job_title',
        'employee_residence','remote_ratio','company_location','company_size']]

y = df['salary_in_usd']

x = pd.get_dummies(x,drop_first = True)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=42)

model = LinearRegression()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("mean_squared_error",mean_squared_error(y_test,y_pred))
print("r2 Score", r2_score(y_test,y_pred))

model1 = RandomForestRegressor(n_estimators=200, max_depth=20, min_samples_split=5, random_state=42)


model1.fit(x_train,y_train)

y_pred1 = model1.predict(x_test)

print("mean_squarred_error",mean_squared_error(y_test,y_pred1))
print("r2_score",r2_score(y_test,y_pred1))