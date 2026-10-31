# KNN Business Case: predict Premium Membership from customer behavior features.

import pandas as pd  # Tabular data and DataFrame support
from sklearn.metrics import accuracy_score  # Compare predicted vs actual labels on test set
from sklearn.model_selection import train_test_split  # Hold out 20% for unbiased evaluation
from sklearn.neighbors import KNeighborsClassifier  # k-nearest neighbors classification
from sklearn.preprocessing import StandardScaler  # Zero mean / unit variance scaling for KNN distance


def get_raw_data():
    """
    Return the retail customer dataset as a dictionary of parallel lists.

    Each list has 15 rows: one customer per row.
    Premium_Member is the label we want to predict (Yes / No).
    """
    # Feature and label columns for 15 customers
    data = {
        "Age": [
            22, 25, 28, 30, 35, 38, 42, 45, 50, 55,
            27, 32, 40, 48, 52,
        ],
        "Monthly_Spending": [
            200, 250, 300, 450, 600, 650, 800, 900, 1000, 1100,
            280, 500, 750, 950, 1050,
        ],
        "Store_Visits": [
            2, 3, 3, 5, 7, 8, 10, 11, 12, 13,
            2, 6, 9, 11, 12,
        ],
        "Premium_Member": [
            "No", "No", "No", "No", "Yes",
            "Yes", "Yes", "Yes", "Yes", "Yes",
            "No", "No", "Yes", "Yes", "Yes",
        ],
    }
    return data  # Raw data before modeling


def build_dataframe(data):
    """
    Convert the raw dictionary into a Pandas DataFrame (Step 1).

    Args:
        data: Dict with column names as keys and list values as rows.

    Returns:
        pd.DataFrame: One row per customer, one column per field.
    """
    df = pd.DataFrame(data)  # Step 1: raw data → DataFrame
    return df


def split_features_and_target(df):
    """
    Separate predictors (X) from the membership label (y) (Steps 2–3).

    Args:
        df: Full customer table including Premium_Member.

    Returns:
        X: Feature matrix (Age, Monthly_Spending, Store_Visits).
        y: Target vector (Premium_Member).
    """
    feature_columns = ["Age", "Monthly_Spending", "Store_Visits"]  # Step 2: input features
    X = df[feature_columns]  # All rows, feature columns only
    y = df["Premium_Member"]  # Step 3: target column
    return X, y


def split_train_test(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets (Step 4).

    80% train / 20% test by default; random_state keeps the split reproducible.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    """
    Standardize features so KNN distances are not dominated by large scales (Step 5).

    Fit scaler on training data only, then apply the same transform to test data
    to avoid leaking test-set statistics into training.
    """
    scaler = StandardScaler()  # Step 5: create scaler
    X_train_scaled = scaler.fit_transform(X_train)  # Learn mean/std from train, transform train
    X_test_scaled = scaler.transform(X_test)  # Apply train statistics to test
    return scaler, X_train_scaled, X_test_scaled


def train_knn_model(X_train_scaled, y_train, n_neighbors=3):
    """
    Build and fit a KNN classifier (Steps 6–7).

    Args:
        X_train_scaled: Scaled training features.
        y_train: Training labels.
        n_neighbors: Number of neighbors to vote (assignment uses k=3).

    Returns:
        Fitted KNeighborsClassifier ready for predict().
    """
    model = KNeighborsClassifier(n_neighbors=n_neighbors)  # Step 6: KNN with k=3
    model.fit(X_train_scaled, y_train)  # Step 7: train on scaled training set
    return model


def compute_test_accuracy(model, X_test_scaled, y_test):
    """
    Predict on the held-out test set and return accuracy (Step 8).

    Accuracy = fraction of test customers where prediction matches Premium_Member.
    """
    y_pred = model.predict(X_test_scaled)  # Class labels for test rows
    accuracy = accuracy_score(y_test, y_pred)  # Step 8: accuracy metric
    return accuracy


def predict_new_customer(model, scaler, age, monthly_spending, store_visits):
    """
    Predict Premium_Member for one new customer (Step 9).

    The new row must be scaled with the same StandardScaler fitted on training data.
    """
    new_customer = pd.DataFrame(
        {
            "Age": [age],
            "Monthly_Spending": [monthly_spending],
            "Store_Visits": [store_visits],
        }
    )  # Step 9: business case customer profile
    new_customer_scaled = scaler.transform(new_customer)  # Same scaling as train/test
    membership_prediction = model.predict(new_customer_scaled)[0]  # Single predicted label
    return new_customer, membership_prediction


def main():
    """Run the full pipeline: DataFrame → split → scale → KNN → accuracy → new prediction."""
    data = get_raw_data()  # Load assignment dataset
    df = build_dataframe(data)  # Step 1
    print("Dataset:")  # Show full table for verification
    print(df)
    print()

    X, y = split_features_and_target(df)  # Steps 2–3
    X_train, X_test, y_train, y_test = split_train_test(X, y)  # Step 4: 80/20 split

    scaler, X_train_scaled, X_test_scaled = scale_features(X_train, X_test)  # Step 5

    model = train_knn_model(X_train_scaled, y_train)  # Steps 6–7

    accuracy = compute_test_accuracy(model, X_test_scaled, y_test)  # Step 8
    print(f"Model accuracy (test set): {accuracy:.2%}")
    print()

    new_customer, membership_prediction = predict_new_customer(
        model, scaler, age=37, monthly_spending=700, store_visits=8
    )  # Step 9: Age=37, Spending=700, Visits=8

    print("New customer:")  # Display input features
    print(new_customer.to_string(index=False))
    print(f"\nPremium Member prediction: {membership_prediction}")  # Final answer: Yes or No


if __name__ == "__main__":
    main()  # Execute pipeline when script is run directly
