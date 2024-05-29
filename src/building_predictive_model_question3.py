import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv('../data/merged/merged_data.csv')

# Drop all categorical variables
categorical_cols = df.select_dtypes(include=['object']).columns
pokemon_data_numerical = df.drop(categorical_cols, axis=1)

# Drop the 'capture_rate' field
pokemon_data_numerical.drop('capture_rate', axis=1, inplace=True)

# Splitting the data into features and target variable
X = pokemon_data_numerical.drop('hasMegaEvolution', axis=1)
y = pokemon_data_numerical['hasMegaEvolution']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
rf= RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the numerical dataset
rf.fit(X_train, y_train)

# Predict on the test set
y_pred = rf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(accuracy)
print(report)