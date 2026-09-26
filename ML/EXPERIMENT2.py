import math

def compute_dispersion(name, data):
    n = len(data)
    mean_val = sum(data) / n

    # Population Variance and Standard Deviation (per lab manual formula / n)
    pop_variance = sum((x - mean_val) ** 2 for x in data) / n
    pop_std_dev = math.sqrt(pop_variance)

    # Sample Variance and Standard Deviation (/ n - 1)
    sample_variance = sum((x - mean_val) ** 2 for x in data) / (n - 1)
    sample_std_dev = math.sqrt(sample_variance)

    print(f"Results for {name} (N = {n}):")
    print(f"  Mean                      : {mean_val:.4f}")
    print(f"  Population Variance (σ²)  : {pop_variance:.4f}")
    print(f"  Population Std Dev (σ)    : {pop_std_dev:.4f}")
    print(f"  Sample Variance (s²)      : {sample_variance:.4f}")
    print(f"  Sample Std Dev (s)        : {sample_std_dev:.4f}\n")


X1 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5, 1, 2, 3, 4, 2, 5, 1, 3, 2, 1, 2, 1, 1, 1, 2]
X2 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5, 1, 2, 3, 4, 2, 5, 1, 3, 2, 1, 2, 1, 1, 1, 2000]
X3 = [1, 2, 3, 10, 20, 30, 100, 200, 300, 1000, 2000, 3000]

compute_dispersion("X1", X1)
compute_dispersion("X2", X2)
compute_dispersion("X3", X3)