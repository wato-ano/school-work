import numpy as np

rng = np.random.default_rng(42)
er_bed_capacity = 50.0
mean_patients = 40.0
std_patients = 8.0
N_simulations = 100_000

# Generate 100,000 random daily ER patient influx scenarios
patient_influx = rng.normal(mean_patients, std_patients, N_simulations)

# Count how many scenarios exceeded bed capacity
overflow_cases = patient_influx > er_bed_capacity
overflow_probability = overflow_cases.mean()

print(f"Estimated ER Overflow Probability: {overflow_probability:.2%}")
print(f"Number of Overflow Disasters: {overflow_cases.sum()} out of {N_simulations} simulated days")