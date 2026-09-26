import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# ==========================================
# 1. NumPy: Numerical Array Operations
# ==========================================
print("--- 1. NumPy Demonstration ---")
# Creating arrays and matrix math
arr = np.array([10.5, 20.2, 30.8, 40.1, 50.6])
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

dot_product = np.dot(matrix_a, matrix_b)
print(f"NumPy 1D Array Mean: {np.mean(arr):.2f}, Std: {np.std(arr):.2f}")
print("NumPy Matrix Dot Product (A @ B):\n", dot_product)
print()

# ==========================================
# 2. Pandas: Data Manipulation & Cleaning
# ==========================================
print("--- 2. Pandas Demonstration ---")
# Load dataset into DataFrame
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# Adding a synthetic categorical column and cleaning demonstration
df["species_name"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

print("Pandas DataFrame Head (First 3 rows):")
print(df.head(3))
print(f"\nDataFrame Shape: {df.shape}")
print(f"Missing Values Check:\n{df.isnull().sum().to_dict()}")
print(f"Value Counts of Target:\n{df['species_name'].value_counts().to_dict()}")
print()

# ==========================================
# 3. Scikit-learn: Preprocessing & Splitting
# ==========================================
print("--- 3. Scikit-learn Demonstration ---")
X = iris.data
y = iris.target

# Data splitting (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# Feature standardization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training Features Shape: {X_train_scaled.shape}")
print(f"Testing Features Shape : {X_test_scaled.shape}")
print()

# ==========================================
# 4. TensorFlow / Keras: Deep Learning Model
# ==========================================
print("--- 4. TensorFlow Demonstration ---")
# Build a Sequential Neural Network
tf.random.set_seed(42)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")
])

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train model
history = model.fit(
    X_train_scaled,
    y_train,
    epochs=50,
    batch_size=8,
    verbose=0
)

# Evaluate model using Scikit-learn metrics
y_pred_probs = model.predict(X_test_scaled, verbose=0)
y_pred = np.argmax(y_pred_probs, axis=1)

final_accuracy = accuracy_score(y_test, y_pred)
print(f"TensorFlow Model Test Accuracy: {final_accuracy * 100:.2f}%\n")
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))