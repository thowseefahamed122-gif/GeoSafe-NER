import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv("landslide_data.csv")

# Input features
X = data[[
    "rainfall",
    "soil_moisture",
    "slope",
    "water_level"
]]

# Target value
y = data["risk"]

# Split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the AI model
model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

# Train the AI model
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("========================================")
print("       AI LANDSLIDE PREDICTION")
print("========================================")

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Test new environmental conditions
new_data = [[85, 78, 40, 70]]

prediction = model.predict(new_data)

print("\nNew Environmental Data:")
print("Rainfall       : 85 mm")
print("Soil Moisture  : 78%")
print("Slope          : 40°")
print("Water Level    : 70%")

if prediction[0] == 1:
    print("\n🚨 AI RESULT: HIGH LANDSLIDE RISK")
else:
    print("\n✅ AI RESULT: LOW LANDSLIDE RISK")

print("========================================")