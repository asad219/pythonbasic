import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Decision Tree Classifier
from sklearn.model_selection import train_test_split

# Raw data
data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 55],
    "Monthly_Income": [3000, 4000, 5000, 6500, 7000, 8500, 9000, 10000],
    "Credit_Score": [500, 550, 600, 650, 680, 720, 750, 800],
    "Loan_Approved": ["No", "No", "No", "Yes", "Yes", "Yes", "Yes", "Yes"],
}

# Convert raw data into a DataFrame
df = pd.DataFrame(data)
print("Dataset:")
print(df)
print()

# Input features (X) and target (y)
feature_columns = ["Age", "Monthly_Income", "Credit_Score"] # List of feature columns
X = df[feature_columns]
y = df["Loan_Approved"]

# Create and train Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# New customer (update these if your assignment gives different values)
new_customer = pd.DataFrame(
    {
        "Age": [32],
        "Monthly_Income": [5000],
        "Credit_Score": [600],
    }
)

prediction = model.predict(new_customer)[0]
print("New customer:")
print(new_customer.to_string(index=False))
print(f"\nLoan approved? {prediction}")
