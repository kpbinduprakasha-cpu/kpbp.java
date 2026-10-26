
from sklearn.linear_model import LinearRegression

# Training data
hours = [[1], [2], [3], [4], [5]]
marks = [20, 30, 40, 50, 60]

# Create the model
model = LinearRegression()

# Train the model
model.fit(hours, marks)

# Predict marks for 6 hours
prediction = model.predict([[6]])

print("Predicted marks:", prediction[0])
