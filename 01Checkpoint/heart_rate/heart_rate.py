def calculate_target_heart_rate(age):
    max_heart_rate = 220 - age
    min_target_rate = 0.65 * max_heart_rate
    max_target_rate = 0.85 * max_heart_rate
    return min_target_rate, max_target_rate

age = int(input("Enter your age: "))
min_rate, max_rate = calculate_target_heart_rate(age)
print(f"Your target heart rate range for strengthening your heart is between {min_rate:.0f} and {max_rate:.0f} beats per minute.")