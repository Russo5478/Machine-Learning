from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = load_breast_cancer()
print(data.get('feature_names'))

X = data.data
Y = data.target

X_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

clf1 = DecisionTreeClassifier()
clf1.fit(X_train, y_train)

clf2 = RandomForestClassifier()
clf2.fit(X_train, y_train)

print(f"Decision Tree: {clf1.score(x_test, y_test)}")
print(f"Random Tree: {clf2.score(x_test, y_test)}")

# New dataset for testing
new_data = [[13.08, 15.71, 85.63, 520.0, 0.1075, 0.127, 0.04568, 0.0311, 0.1967, 0.06811, 0.1852, 0.7477, 1.383, 14.67,
             0.004097, 0.01898, 0.01698, 0.00649, 0.01678, 0.002425, 14.5, 20.49, 96.09, 630.5, 0.1312, 0.2776, 0.189,
             0.07283, 0.3184, 0.08183]]

# Predict using the trained classifiers
prediction1 = clf1.predict(new_data)
prediction2 = clf2.predict(new_data)

print(f"Decision Tree Prediction: {prediction1}")
print(f"Random Forest Prediction: {prediction2}")