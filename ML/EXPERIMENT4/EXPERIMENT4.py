import math
import numpy as np

def compute_metrics(v1, v2):
    a = np.array(v1, dtype=float)
    b = np.array(v2, dtype=float)

    # 1. Cosine Similarity: (A . B) / (||A|| * ||B||)
    dot_product = np.dot(a, b)
    norm_a = math.sqrt(np.dot(a, a))
    norm_b = math.sqrt(np.dot(b, b))
    cosine_sim = dot_product / (norm_a * norm_b)

    # 2. Euclidean Distance: sqrt(sum((a_i - b_i)^2))
    euclidean_dist = math.sqrt(np.sum((a - b) ** 2))

    return cosine_sim, euclidean_dist


# Input vectors
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [1, 3, 5, 7, 9, 7, 5, 3, 1, 0]

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [1, 3, 5, 7, 9, 7, 5, 3, 1, 0]

cos_ab, euc_ab = compute_metrics(A, B)
cos_xy, euc_xy = compute_metrics(X, Y)

print(f"Vectors (A, B):")
print(f"  Cosine Similarity : {cos_ab:.6f}")
print(f"  Euclidean Distance: {euc_ab:.6f}\n")

print(f"Vectors (X, Y):")
print(f"  Cosine Similarity : {cos_xy:.6f}")
print(f"  Euclidean Distance: {euc_xy:.6f}")