import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    "Salary": [3000, 4500, 5000, 6500, 7000, 8000, 4000, 9000, 5500, 7500],
    "Experience": [1, 2, 3, 5, 6, 8, 2, 10, 4, 7],
    "Overtime_Hours": [20, 18, 15, 8, 5, 3, 22, 2, 12, 6],
    "Left_Company": [ "Yes","Yes", "Yes","No","No","No","Yes","No","Yes","No",
    ],
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)
print()

feature_columns = ["Salary", "Experience", "Overtime_Hours"]
X = df[feature_columns]
y = df["Left_Company"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy (test set): {accuracy:.2%}")
print()

new_employee = pd.DataFrame(
    {
        "Salary": [6500],
        "Experience": [3],
        "Overtime_Hours": [12],
    }
)

prediction = model.predict(new_employee)[0]
print("New employee:")
print(new_employee.to_string(index=False))
print(f"\nWill the employee leave the company? {prediction}")
