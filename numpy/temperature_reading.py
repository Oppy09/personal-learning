import numpy as np
import timeit

# size of data
num_of_readings = 1000000

# generate temperature array
np.random.seed(21) # to return the same results each time code is run
mean_temp = 36.0
std_dev_temp = 10.0
temp_data = np.random.normal(loc=mean_temp, scale=std_dev_temp,size=num_of_readings)

print("Array Size:", temp_data.size) # print size of array
print(temp_data[:5]) # print first 5 readings

# Numpy mathematical effectiveness
# Calculate mean using standard python
def calculate_mean(data):
    total = 0
    count = 0
    for el in data:
        total += el
        count += 1
    return total / count

print(f"Standard Python Mean: {calculate_mean(temp_data)}")
# Timing the Standard Python Loop
print("Standard Python Time:", timeit.timeit("calculate_mean(temp_data)", globals=globals(), number=5))
''' 
globals=globals() tells timeit which namespace to use when it evaluates the string 
`calculate_mean(temp_data)`, python may not know what it means without it
number=5 runs the timing code 5 times to give a more stable average and reduces noise
from one-off fluctuations
returned value is total time for all 5 runs
'''
# to get the total time per run
total_time = timeit.timeit("calculate_mean(temp_data)", globals=globals(), number=5)
print("Time per run:", total_time / 5)

# Calculate mean using Numpy
def calculate_mean_numpy(data):
    return np.mean(data)
print(f"Numpy mean:", calculate_mean_numpy(temp_data))

# Timing the Numpy method
print("Numpy time:", timeit.timeit("calculate_mean_numpy(temp_data)", globals=globals(), number=5))

# 