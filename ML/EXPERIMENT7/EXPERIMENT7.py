import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# 1. Load Iris flower dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Define candidate values of k and 10-fold CV scheme
k_values = [1, 3, 5, 7]
kf = KFold(n_splits=10, shuffle=True, random_state=42)

mean_accuracies = []

# 3. Evaluate each k using 10-fold cross validation
print("--- 10-Fold Cross-Validation Performance ---")
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=kf, scoring="accuracy")
    avg_accuracy = scores.mean()
    mean_accuracies.append(avg_accuracy)
    print(f"k = {k}: Mean Accuracy = {avg_accuracy:.4f} ({avg_accuracy*100:.2f}%)")

# 4. Plot line chart for k vs. accuracy
plt.figure(figsize=(7, 4.5))
plt.plot(
    k_values,
    [acc * 100 for acc in mean_accuracies],
    marker="o",
    color="b",
    linestyle="-",
    linewidth=2,
    markersize=7,
)

for k, acc in zip(k_values, mean_accuracies):
    plt.annotate(
        f"{acc*100:.2f}%",
        (k, acc * 100),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontweight="bold",
    )

plt.title("k-NN 10-Fold Cross-Validation Accuracy vs. k", fontsize=12)
plt.xlabel("Value of k", fontsize=11)
plt.ylabel("Mean Accuracy (%)", fontsize=11)
plt.xticks(k_values)
plt.ylim(90, 100)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()