import numpy as np

# Time in weeks and Tumor Volume in cm^3
weeks = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
volume = np.array([2.0, 2.8, 3.5, 3.9, 4.1, 4.15, 4.18])
growth_rate = np.zeros_like(volume)

# Forward difference (start), Central (middle), Backward (end)
growth_rate[0] = (volume[1] - volume[0]) / (weeks[1] - weeks[0])
for i in range(1, len(weeks) - 1):
    growth_rate[i] = (volume[i + 1] - volume[i - 1]) / (weeks[i + 1] - weeks[i - 1])
growth_rate[-1] = (volume[-1] - volume[-2]) / (weeks[-1] - weeks[-2])

for t, vol, rate in zip(weeks, volume, growth_rate):
    print(f"Week {t:.0f}: Vol = {vol:.2f} cm^3, Est. Growth Rate = {rate:.2f} cm^3/week")