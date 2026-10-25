"""
Machine Learning study examples — one small demo per topic.

How to run:
    python ml.py

Dependencies (install in a virtual environment):
    pip install scikit-learn numpy
"""

# Allows modern type hints (e.g. list[str]) on older Python versions.
from __future__ import annotations

# NumPy: fast arrays and math — ML libraries expect data in this form.
import numpy as np

# KMeans: groups unlabeled points into K clusters (unsupervised).
from sklearn.cluster import KMeans

# LinearRegression: predict numbers. LogisticRegression: predict classes (0/1).
from sklearn.linear_model import LinearRegression, LogisticRegression

# Metrics to measure how good a classifier is.
from sklearn.metrics import (
    accuracy_score,       # % of all predictions that were correct
    confusion_matrix,     # table of TN, FP, FN, TP
    f1_score,             # balance between precision and recall
    mean_absolute_error,  # regression: average size of prediction mistakes (easy to read)
    precision_score,      # of predicted "yes", how many were really yes?
    recall_score,         # of actual "yes", how many did we find?
    roc_auc_score,        # single number summarizing ROC quality (0.5–1.0)
    roc_curve,            # TPR vs FPR at many decision thresholds
)

# Splits data into train and test sets so we can check generalization.
from sklearn.model_selection import train_test_split


def demo_supervised_learning() -> None:
    """
    SUPERVISED LEARNING
    -------------------
    You provide features (X) and correct labels (y).
    The model learns the mapping X → y, then predicts y for new X.

    This demo uses linear regression: predict exam score from study hours.
    """
    print("\n=== Supervised Learning (Linear Regression) ===")

    # X = input features. Shape (n_samples, n_features).
    # Each row is one student; one column = hours studied.
    X = np.array([[1], [2], [3], [4], [5], [6]])

    # y = target (what we want to predict): exam score for each student.
    y = np.array([50, 55, 65, 70, 80, 85])

    # Create an empty linear model (line: score = m * hours + b).
    model = LinearRegression()

    # fit() = "learn" from X and y (find best m and b).
    model.fit(X, y)

    # Ask: what score for a student who studied 7 hours?
    new_hours = np.array([[7]])

    # predict() returns an array; [0] takes the first (only) prediction.
    predicted_score = model.predict(new_hours)[0]
    print(f"After 7 hours study, predicted score ≈ {predicted_score:.1f}")


def demo_unsupervised_learning() -> None:
    """
    UNSUPERVISED LEARNING
    ---------------------
    Only X — no y labels. The algorithm finds patterns (here: 2 groups).

    K-Means puts each point into one of K clusters by distance to cluster centers.
    """
    print("\n=== Unsupervised Learning (K-Means clustering) ===")

    # Fixed random seed so results are the same every run (for learning).
    rng = np.random.default_rng(42)

    # Simulate 30 points near (2, 2) — e.g. "budget shoppers".
    cluster_a = rng.normal(loc=[2, 2], scale=0.4, size=(30, 2))

    # Simulate 30 points near (6, 6) — e.g. "premium shoppers".
    cluster_b = rng.normal(loc=[6, 6], scale=0.4, size=(30, 2))

    # Stack into one dataset: 60 rows, 2 columns (features per customer).
    X = np.vstack([cluster_a, cluster_b])

    # n_clusters=2: we want two groups. n_init: run K-Means several times for stability.
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)  # pyright: ignore[reportArgumentType]

    # fit_predict: learn centers and assign each row a cluster label (0 or 1).
    labels = kmeans.fit_predict(X)

    print(f"Found 2 groups. First 5 labels: {labels[:5]}")
    # cluster_centers_: average position of each group in 2D space.
    print(f"Group centers:\n{kmeans.cluster_centers_}")


def demo_reinforcement_learning() -> None:
    """
    REINFORCEMENT LEARNING (simplified)
    -----------------------------------
    An "agent" picks an action, gets reward (0 or 1), and updates beliefs.

    This is a 2-armed bandit: two buttons; button 1 pays off more often.
    Epsilon-greedy: usually pick the best-known action, sometimes try the other (explore).
    """
    print("\n=== Reinforcement Learning (toy bandit) ===")

    # Hidden truth: probability of reward=1 if we pick action 0 or 1.
    true_rewards = [0.2, 0.8]

    # How many times we tried each action (for running average).
    counts = [0, 0]

    # Our current guess of average reward per action (starts at 0).
    value_estimates = [0.0, 0.0]

    rng = np.random.default_rng(0)

    # Repeat 200 times: choose action → get reward → update estimate.
    for step in range(200):
        # 10% of the time: random action (exploration).
        if rng.random() < 0.1:
            action = rng.integers(0, 2)
        else:
            # 90%: pick action with highest estimated reward (exploitation).
            action = int(np.argmax(value_estimates))

        # Simulate environment: reward 1 with probability true_rewards[action].
        reward = 1.0 if rng.random() < true_rewards[action] else 0.0

        counts[action] += 1

        # Incremental mean update: new_avg += (reward - old_avg) / count
        value_estimates[action] += (reward - value_estimates[action]) / counts[action]

    best_action = int(np.argmax(value_estimates))
    print(f"Learned best action: {best_action} (higher true reward)")
    print(f"Estimated rewards: {value_estimates}")


def demo_train_test_split() -> None:
    """
    TRAINING vs TESTING
    -------------------
    Train on one subset; evaluate on held-out data the model never saw.

    We check quality with average prediction error (not R² — that is a separate topic).
    """
    print("\n=== Training vs Testing Data ===")

    # Feature: day index 0..19, shaped as column vector for sklearn.
    X = np.arange(20).reshape(-1, 1)

    # Target: sales ≈ 2 * day + 5, plus small random noise (real data is never perfect).
    y = 2 * X.ravel() + 5 + rng_noise(20)

    # 75% train, 25% test. random_state=42 keeps the same split each run.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = LinearRegression()

    # Learn ONLY from training data — test set is locked away until evaluation.
    model.fit(X_train, y_train)

    # Mean absolute error: on average, predictions are off by this many sales units.
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    train_mae = mean_absolute_error(y_train, train_pred)
    test_mae = mean_absolute_error(y_test, test_pred)

    print(f"Train size: {len(X_train)}, Test size: {len(X_test)}")
    print(f"Average error on train data: {train_mae:.2f} units")
    print(f"Average error on test data:  {test_mae:.2f} units")
    print("Example on test set (true sales → predicted):")
    for i in range(min(3, len(y_test))):
        print(f"  {y_test[i]:.1f} → {test_pred[i]:.1f}")
    print("(If test error is much bigger than train error, model may be overfitting.)")


def rng_noise(n: int) -> np.ndarray:
    """Return n random values (mean 0, spread 2) to make fake sales data less perfect."""
    return np.random.default_rng(42).normal(0, 2, size=n)


def demo_linear_regression() -> None:
    """
    LINEAR REGRESSION
    -----------------
    Predict a continuous number. After fit(), coef_ is slope (m), intercept_ is b.
    """
    print("\n=== Linear Regression ===")

    # Independent variable: house size in square feet.
    size_sqft = np.array([[800], [1200], [1500], [2000], [2500]])

    # Dependent variable: sale price in dollars.
    price = np.array([200000, 280000, 350000, 420000, 500000])

    model = LinearRegression()
    model.fit(size_sqft, price)

    # Predict price for 1800 sqft (not in training table — true prediction use case).
    pred = model.predict(np.array([[1800]]))[0]

    print(f"1800 sqft → predicted price ≈ ${pred:,.0f}")
    print(f"Line: price ≈ {model.coef_[0]:.0f} * sqft + {model.intercept_:,.0f}")


def demo_logistic_regression() -> None:
    """
    LOGISTIC REGRESSION
    -------------------
    Binary classification: outputs probability, then class 0 or 1.

    predict_proba returns [P(class 0), P(class 1)] for each row.
    """
    print("\n=== Logistic Regression ===")

    # One feature per email: count of suspicious words.
    X = np.array([[0], [1], [1], [2], [3], [4], [5], [6]])

    # Label: 0 = not spam, 1 = spam.
    y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

    model = LogisticRegression()
    model.fit(X, y)

    # Email with 3 suspicious words.
    test_email = np.array([[3]])

    # Index [0] = first sample, [1] = probability of class 1 (spam).
    prob_spam = model.predict_proba(test_email)[0][1]

    # Hard decision: usually spam if prob >= 0.5 (sklearn default threshold).
    label = model.predict(test_email)[0]

    print(f"Email with 3 suspicious words → P(spam)={prob_spam:.2f}, class={label}")


def demo_confusion_matrix_and_roc() -> None:
    """
    CONFUSION MATRIX, ROC CURVE, AUC
    --------------------------------
    - y_pred: class after threshold (here score >= 0.5 → 1).
    - ROC uses y_scores (probabilities), not just hard 0/1 predictions.
    - AUC: area under ROC curve; 1.0 is ideal ranking of positives above negatives.
    """
    print("\n=== Confusion Matrix, ROC, AUC ===")

    # Ground truth from reality.
    y_true = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 0])

    # Model confidence for class 1 (higher = more likely positive).
    y_scores = np.array([0.1, 0.4, 0.35, 0.8, 0.9, 0.2, 0.7, 0.3, 0.85, 0.15])

    # Turn scores into 0/1 labels using cutoff 0.5.
    y_pred = (y_scores >= 0.5).astype(int)

    # Rows/cols: actual vs predicted (see sklearn docs for layout).
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion matrix [[TN, FP], [FN, TP]]:")
    print(cm)
    print("TN=correct negatives, FP=false alarm, FN=missed positive, TP=correct positive")

    # fpr = false positive rate, tpr = true positive rate (recall), thresholds used.
    fpr, tpr, thresholds = roc_curve(y_true, y_scores)

    # One scalar summary of the whole ROC (threshold-independent).
    auc = roc_auc_score(y_true, y_scores)

    print(f"ROC: {len(thresholds)} thresholds; example TPR@first point={tpr[1]:.2f}")
    print(f"ROC AUC = {auc:.3f} (closer to 1 is better)")


def demo_classification_metrics() -> None:
    """
    ACCURACY, PRECISION, RECALL, F1
    --------------------------------
    All compare y_true vs y_pred (hard 0/1 predictions).

    Manual check for this example:
        TP=4, FP=1, FN=1, TN=4 → 8/10 correct → accuracy 0.80
    (Comment in older version said 7/10 — sklearn gives 0.80 with these arrays.)
    """
    print("\n=== Accuracy, Precision, Recall, F1 ===")

    # 5 positive (1), 5 negative (0) — balanced classes for a fair demo.
    y_true = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
    y_pred = np.array([1, 1, 1, 0, 1, 0, 0, 1, 0, 0])

    print(f"Accuracy:  {accuracy_score(y_true, y_pred):.2f}")
    print(f"Precision: {precision_score(y_true, y_pred):.2f}  (of predicted 'yes', how many right)")
    print(f"Recall:    {recall_score(y_true, y_pred):.2f}  (of actual 'yes', how many caught)")
    print(f"F1-Score:  {f1_score(y_true, y_pred):.2f}  (single score mixing precision & recall)")


def main() -> None:
    """Run every demo in study order."""
    print("Machine Learning — topic demos\n" + "=" * 40)

    demo_supervised_learning()
    demo_unsupervised_learning()
    demo_reinforcement_learning()
    demo_train_test_split()
    demo_linear_regression()
    demo_logistic_regression()
    demo_confusion_matrix_and_roc()
    demo_classification_metrics()

    print("\nDone.")


# Only run main() when this file is executed directly (not when imported).
if __name__ == "__main__":
    main()
