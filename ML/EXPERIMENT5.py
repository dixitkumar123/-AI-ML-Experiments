import matplotlib.pyplot as plt
import numpy as np

# Given data
X = np.array([70, 80, 90, 100, 110, 120, 130, 140, 150, 160], dtype=float)
Y = np.array([7, 7, 8, 9, 12, 12, 15, 14, 13, 17], dtype=float)

# 1. Compute means
x_mean = np.mean(X)   # 115.0
y_mean = np.mean(Y)   # 11.4

# 2. Compute parameters using Ordinary Least Squares (OLS)
# w1 (slope) = sum((X - x_mean) * (Y - y_mean)) / sum((X - x_mean)^2)
w1 = np.sum((X - x_mean) * (Y - y_mean)) / np.sum((X - x_mean) ** 2)

# w0 (intercept) = y_mean - w1 * x_mean
w0 = y_mean - w1 * x_mean

# 3. Predict Y for X = 210
x_target = 210.0
y_pred = w0 + w1 * x_target

print(f"Intercept (w0)  : {w0:.6f}")
print(f"Slope (w1)      : {w1:.6f}")
print(f"Regression Eq   : Y_hat = {w0:.4f} + {w1:.4f} * X")
print(f"Predicted Y at X = {x_target}: {y_pred:.4f}")

# 4. Plotting
plt.figure(figsize=(9, 5))
plt.scatter(X, Y, color="blue", s=60, label="Actual Data Points", zorder=3)

# Best fit line
x_vals = np.linspace(60, 220, 100)
y_vals = w0 + w1 * x_vals
plt.plot(
    x_vals,
    y_vals,
    color="red",
    linewidth=2,
    label=f"Fit Line: $\\hat{{Y}} = {w0:.2f} + {w1:.4f}X$",
)

# Target point
plt.scatter(
    [x_target],
    [y_pred],
    color="green",
    marker="*",
    s=200,
    zorder=4,
    label=f"Predicted ({x_target}, {y_pred:.2f})",
)
plt.axvline(x=x_target, color="gray", linestyle="--", alpha=0.6)
plt.axhline(y=y_pred, color="gray", linestyle="--", alpha=0.6)

plt.title("Simple Linear Regression: Advertisement Spending vs Unit Sales", fontsize=12)
plt.xlabel("Amount Spent on Advertisement (X)")
plt.ylabel("Increase in Unit Sale (Y)")
plt.xlim(60, 220)
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()