"""
Die Roll Simulation: Law of Large Numbers

This script simulates rolling a fair six-sided die 10, 100, 1,000, 10,000
and 1,000,000 times using NumPy, and measures how far each face's relative
frequency is from the theoretical probability of 1/6.

Findings:
- As the number of rolls increases, the relative frequency of each face
  converges to 1/6, so the faces become equally distributed.
- The largest gap shrinks in proportion to 1 / sqrt(n). Rolling 100 times
  more often reduced the gap by about a factor of 10, and quadrupling the
  number of rolls should roughly halve it.
- Small samples are noisy: with 10 rolls the largest gap was 0.23 and varied
  widely between seeds, while with 1,000,000 rolls it was about 0.0005.
"""

import numpy as np

# Initialize the random number generator for reproducibility
rng = np.random.default_rng(12345)

iteration = [10, 100, 1000, 10000, 25000, 100000, 1000000]
for i in iteration:
    roll = rng.integers(1, 7, size=i)
    # print(f"Mean of {i} rolls: {roll.mean()}")

    count = np.bincount(roll, minlength=7)[1:]  # Count occurrences of each face (1-6)
    # print(f"Counts for {i} rolls: {count}")
    # print(f"Relative frequencies for {i} rolls: {count / roll.size}\n")
    
    print(f"Largest gap between relative frequencies and theoretical probabilities for {i} rolls: {np.abs(count / roll.size - 1/6).max()}\n")
