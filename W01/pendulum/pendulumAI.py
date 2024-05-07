import math

# Prompt the user to enter the length of the pendulum in meters
length = float(input("Enter the length of the pendulum in meters: "))

# Calculate the time using the given formula
time = 2 * math.pi * (length / 9.81) ** 0.5

# Print the result
print(f"The time it takes for a pendulum of length {length} meters to swing back and forth is {time:.2f} seconds.")