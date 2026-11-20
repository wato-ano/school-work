import numpy as np
import timeit

# 1,000,000 element benchmark array
arr = np.random.default_rng(42).uniform(1.0, 100.0, 1_000_000)

def loop_version():
    res = []
    for val in arr:
        res.append((val / 10.0) ** 2)
    return res

def vectorized_version():
    return (arr / 10.0) ** 2

# Benchmark execution time
loop_time = timeit.timeit(loop_version, number=1)
vec_time = timeit.timeit(vectorized_version, number=3) / 3

print("First 5 values:", np.round(vectorized_version()[:5], 4))
print(f"Loop Time: {loop_time:.4f} s | Vectorized Time: {vec_time:.4f} s")
print(f"Speed-up Factor: {loop_time / vec_time:.1f}x")