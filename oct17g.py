import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


data = {
    "Hours_Studied" : [1,2,3,4,5,6,7,8,9,10],
    "Score" : [35, 40, 50, 55, 60, 65, 70, 75, 85, 90]
}

df = pd.DataFrame(data)

x = df[["Hours_Studied"]]
y = df["Score"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state= 42)

model = LinearRegression()

model.fit(x_train,y_train)
y_pred = model.predict(x_test)


print("mean squared error",mean_squared_error(y_test,y_pred))
print("r^2 score",r2_score(y_test,y_pred))

plt.scatter(x,y,color = "blue",label = "actual data")
plt.plot(x,model.predict(x),color= "red",label = "regression line")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.show()



hours = 7.5
new = pd.DataFrame({"Hours_Studied":[hours]})
predicted_score = model.predict(new)
print(f"predicted score for {hours} hours is {predicted_score[0]:.2f}")