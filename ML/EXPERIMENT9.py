import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

# 1. Load and scale the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Standardizing inputs ensures stable gradient descent optimization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Split dataset: 70% Training and 30% Testing
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.30, random_state=42, stratify=y
)

# 3. Define combinations of architectures and training functions (solvers/optimizers)
experiments = [
    {"hidden_layers": (8,), "solver": "adam", "activation": "relu"},
    {"hidden_layers": (8,), "solver": "sgd", "activation": "relu"},
    {"hidden_layers": (16, 8), "solver": "adam", "activation": "relu"},
    {"hidden_layers": (16, 8), "solver": "lbfgs", "activation": "relu"},
    {"hidden_layers": (10, 10), "solver": "adam", "activation": "tanh"},
    {"hidden_layers": (16, 8, 4), "solver": "adam", "activation": "relu"},
]

results = []

for exp in experiments:
    mlp = MLPClassifier(
        hidden_layer_sizes=exp["hidden_layers"],
        solver=exp["solver"],
        activation=exp["activation"],
        max_iter=500,
        random_state=42,
    )
    mlp.fit(X_train, y_train)
    acc = mlp.score(X_test, y_test)

    arch_str = (
        f"Input(4) -> {list(exp['hidden_layers'])} -> Output(3) "
        f"[{exp['activation']}]"
    )
    results.append(
        {
            "Architecture of Neural network": arch_str,
            "Training function": exp["solver"].upper(),
            "Accuracy": f"{acc * 100:.2f}%",
        }
    )

results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))