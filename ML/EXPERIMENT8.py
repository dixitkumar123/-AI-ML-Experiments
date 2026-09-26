import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 1. Dataset Preparation
data = {
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rainy", "Rainy", "Rainy", "Overcast",
                "Sunny", "Sunny", "Rainy", "Sunny", "Overcast", "Overcast", "Rainy"],
    "Temp": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool",
             "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal",
                 "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "Windy": [False, True, False, False, False, True, True, False,
              False, False, True, True, False, True],
    "Play": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No",
             "Yes", "Yes", "Yes", "Yes", "Yes", "No"],
}

df = pd.DataFrame(data)

# 2. Encoding Categorical Features
feature_cols = ["Outlook", "Temp", "Humidity", "Windy"]
encoder = OrdinalEncoder()
X = encoder.fit_transform(df[feature_cols])
y = df["Play"].map({"No": 0, "Yes": 1}).values

# 3. Train/Test Split (10 Train samples, 4 Test samples)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=4, train_size=10, random_state=42
)

# 4. Evaluating Configurations with Different Parameters & 10-Fold CV
param_configs = [
    {
        "name": "Criterion: Gini (Default, Max Depth: None)",
        "model": DecisionTreeClassifier(criterion="gini", random_state=42),
    },
    {
        "name": "Criterion: Entropy (Information Gain)",
        "model": DecisionTreeClassifier(criterion="entropy", random_state=42),
    },
    {
        "name": "Max Depth: 2 (Gini)",
        "model": DecisionTreeClassifier(criterion="gini", max_depth=2, random_state=42),
    },
    {
        "name": "Min Samples Split: 4 (Gini)",
        "model": DecisionTreeClassifier(criterion="gini", min_samples_split=4, random_state=42),
    },
]

print("--- Train/Test (10 vs 4) and 10-Fold CV Performance ---")
kf = KFold(n_splits=10, shuffle=True, random_state=42)

for cfg in param_configs:
    clf = cfg["model"]
    clf.fit(X_train, y_train)
    test_acc = clf.score(X_test, y_test)
    cv_scores = cross_val_score(clf, X, y, cv=kf)
    print(f"Configuration: {cfg['name']}")
    print(f"  Hold-out Test Accuracy (4 samples): {test_acc * 100:.2f}%")
    print(f"  10-Fold CV Mean Accuracy           : {cv_scores.mean() * 100:.2f}%\n")

# 5. Tree Visualization
default_dt = DecisionTreeClassifier(criterion="gini", random_state=42)
default_dt.fit(X, y)

plt.figure(figsize=(10, 6))
plot_tree(
    default_dt,
    feature_names=feature_cols,
    class_names=["No", "Yes"],
    filled=True,
    rounded=True,
)
plt.title("Trained Decision Tree (Play Tennis Dataset)")
plt.tight_layout()
plt.show()