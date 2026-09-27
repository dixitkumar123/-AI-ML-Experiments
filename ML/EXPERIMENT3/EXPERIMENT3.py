import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Load Iris dataset
iris = load_iris()
X = iris.data         # 150 samples x 4 features
y = iris.target
target_names = iris.target_names

# 2. Standardize features to mean = 0, variance = 1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Apply PCA to reduce dimensionality from 4 to 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Summary of variance explained
var_ratio = pca.explained_variance_ratio_
print(f"Variance explained by PC1: {var_ratio[0]*100:.2f}%")
print(f"Variance explained by PC2: {var_ratio[1]*100:.2f}%")
print(f"Total variance retained: {np.sum(var_ratio)*100:.2f}%\n")

# 4. Display sample transformed coordinates
df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["Species"] = [target_names[i] for i in y]
print(df_pca.head())

# 5. Plot the 2D projection
plt.figure(figsize=(8, 6))
colors = ["navy", "turquoise", "darkorange"]
markers = ["o", "s", "^"]

for i, (color, marker, target_name) in enumerate(zip(colors, markers, target_names)):
    plt.scatter(
        X_pca[y == i, 0],
        X_pca[y == i, 1],
        color=color,
        marker=marker,
        alpha=0.85,
        edgecolor="k",
        s=50,
        label=target_name,
    )

plt.title("PCA of Iris Dataset (4D to 2D Projection)", fontsize=13)
plt.xlabel(f"Principal Component 1 ({var_ratio[0]*100:.2f}% Variance)")
plt.ylabel(f"Principal Component 2 ({var_ratio[1]*100:.2f}% Variance)")
plt.legend(loc="best")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()