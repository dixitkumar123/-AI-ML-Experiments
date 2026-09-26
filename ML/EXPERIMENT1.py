import statistics
from collections import Counter

def compute_statistics(name, data):
    # Mean
    mean_val = sum(data) / len(data)

    # Median
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 != 0:
        median_val = sorted_data[n // 2]
    else:
        median_val = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    # Mode
    counts = Counter(data)
    max_freq = max(counts.values())
    if max_freq == 1:
        mode_val = "No Mode (All unique)"
    else:
        modes = [k for k, v in counts.items() if v == max_freq]
        mode_val = ", ".join(map(str, sorted(modes)))

    print(f"Results for {name}:")
    print(f"  Mean   : {mean_val:.4f}")
    print(f"  Median : {median_val}")
    print(f"  Mode   : {mode_val}\n")


X1 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5, 1, 2, 3, 4, 2, 5, 1, 3, 2, 1, 2, 1, 1, 1, 2]
X2 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5, 1, 2, 3, 4, 2, 5, 1, 3, 2, 1, 2, 1, 1, 1, 2000]
X3 = [1, 2, 3, 10, 20, 30, 100, 200, 300, 1000, 2000, 3000]

compute_statistics("X1", X1)
compute_statistics("X2", X2)
compute_statistics("X3", X3)