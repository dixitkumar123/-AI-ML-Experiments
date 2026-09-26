import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# 1. Load Iris Dataset
iris = load_iris()
X = iris.data   # shape: (150, 4)
y = iris.target   # classes: 0, 1, 2
feature_names = iris.feature_names
classes = np.unique(y)
num_features = X.shape[1]

# 2. Overall Mean vector (m)
overall_mean = np.mean(X, axis=0)

# 3. Within-Class Scatter Matrix (S_W)
S_W = np.zeros((num_features, num_features))
for c in classes:
    X_c = X[y == c]
    mean_c = np.mean(X_c, axis=0)
    # Compute sum of outer products: sum((x - m_i)(x - m_i)^T)
    scatter_c = np.dot((X_c - mean_c).T, (X_c - mean_c))
    S_W += scatter_c

# 4. Between-Class Scatter Matrix (S_B)
S_B = np.zeros((num_features, num_features))
for c in classes:
    X_c = X[y == c]
    n_c = X_c.shape[0]
    mean_c = np.mean(X_c, axis=0)
    diff = (mean_c - overall_mean).reshape(-1, 1)
    S_B += n_c * np.dot(diff, diff.T)

# 5. Total Scatter Matrix (S_T)
diff_total = X - overall_mean
S_T = np.dot(diff_total.T, diff_total)

# 6. Verify Additive Property: S_T == S_W + S_B
is_additive = np.allclose(S_T, S_W + S_B)

# Summary of matrix traces (scalar overall variance metric)
trace_W = np.trace(S_W)
trace_B = np.trace(S_B)
trace_T = np.trace(S_T)

print("--- Scatter Matrix Dimensions & Additive Check ---")
print(f"S_T == S_W + S_B: {is_additive}")
print(f"Trace(S_W) : {trace_W:.4f}")
print(f"Trace(S_B) : {trace_B:.4f}")
print(f"Trace(S_T) : {trace_T:.4f}\n")

print("--- Within-Class Scatter Matrix (S_W) ---")
print(np.round(S_W, 4))
print("\n--- Between-Class Scatter Matrix (S_B) ---")
print(np.round(S_B, 4))
print("\n--- Total Scatter Matrix (S_T) ---")
print(np.round(S_T, 4))