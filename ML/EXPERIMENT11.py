import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Load Iris Dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split dataset: 70% Training and 30% Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# Function to align unsupervised cluster indices with ground-truth classes
def evaluate_cluster_accuracy(y_true, cluster_labels):
    dim = max(cluster_labels.max(), y_true.max()) + 1
    cost_matrix = np.zeros((dim, dim), dtype=np.int64)
    for i in range(len(cluster_labels)):
        cost_matrix[cluster_labels[i], y_true[i]] += 1
    # Hungarian algorithm to find optimal 1-to-1 cluster-to-class alignment
    row_ind, col_ind = linear_sum_assignment(cost_matrix.max() - cost_matrix)
    return cost_matrix[row_ind, col_ind].sum() / len(y_true)


# K-Means algorithm supporting varied distance metrics
def fit_kmeans(data, k, metric="euclidean", max_iter=300, random_state=42):
    np.random.seed(random_state)
    initial_indices = np.random.choice(len(data), k, replace=False)
    centroids = data[initial_indices].copy()

    for _ in range(max_iter):
        distances = cdist(data, centroids, metric=metric)
        labels = np.argmin(distances, axis=1)

        new_centroids = np.array(
            [
                (
                    data[labels == j].mean(axis=0)
                    if np.sum(labels == j) > 0
                    else centroids[j]
                )
                for j in range(k)
            ]
        )

        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids

    return centroids


# 3. Experimentation Configurations
experiments = [
    (2, "euclidean", "Euclidean"),
    (3, "euclidean", "Euclidean"),
    (4, "euclidean", "Euclidean"),
    (5, "euclidean", "Euclidean"),
    (3, "cityblock", "Manhattan"),
    (3, "cosine", "Cosine"),
]

table_rows = []

for k, metric_key, metric_name in experiments:
    centroids = fit_kmeans(X_train, k=k, metric=metric_key)

    # Predict test data by assigning each sample to the closest centroid
    test_distances = cdist(X_test, centroids, metric=metric_key)
    test_clusters = np.argmin(test_distances, axis=1)

    acc = evaluate_cluster_accuracy(y_test, test_clusters)
    table_rows.append(
        {
            "Value of K": k,
            "Distance measure": metric_name,
            "Accuracy": f"{acc * 100:.2f}%",
        }
    )

results_df = pd.DataFrame(table_rows)
print(results_df.to_string(index=False))