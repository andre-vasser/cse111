def demonstrate_print():
    """Demonstrate the use of the print() function."""
    print("Hello, World!")
    name = "Alice"
    age = 25
    print(f"My name is {name}, and I'm {age} years old.")

def demonstrate_len():
    """Demonstrate the use of the len() function."""
    fruits = ["apple", "banana", "cherry"]
    print(f"The length of the fruits list is: {len(fruits)}")

def demonstrate_range():
    """Demonstrate the use of the range() function."""
    for i in range(5):
        print(i)

def demonstrate_sum():
    """Demonstrate the use of the sum() function."""
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"The sum of the numbers is: {total}")

def demonstrate_max_min():
    """Demonstrate the use of the max() and min() functions."""
    numbers = [5, 2, 8, 1, 9]
    maximum = max(numbers)
    minimum = min(numbers)
    print(f"The maximum number is: {maximum}")
    print(f"The minimum number is: {minimum}")

def demonstrate_sorted():
    """Demonstrate the use of the sorted() function."""
    names = ["Alice", "Bob", "Charlie", "David"]
    sorted_names = sorted(names)
    print(f"The sorted list of names is: {sorted_names}")

def demonstrate_abs():
    """Demonstrate the use of the abs() function."""
    number = -10
    absolute_value = abs(number)
    print(f"The absolute value of {number} is: {absolute_value}")

def demonstrate_round():
    """Demonstrate the use of the round() function."""
    pi = 3.14159
    rounded_pi = round(pi, 2)
    print(f"The value of pi rounded to 2 decimal places is: {rounded_pi}")

def demonstrate_zip():
    """Demonstrate the use of the zip() function."""
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    zipped = list(zip(names, ages))
    print(f"The zipped list of names and ages is: {zipped}")

def main():
    """Main function to demonstrate the built-in functions."""
    demonstrate_print()
    demonstrate_len()
    demonstrate_range()
    demonstrate_sum()
    demonstrate_max_min()
    demonstrate_sorted()
    demonstrate_abs()
    demonstrate_round()
    demonstrate_zip()

if __name__ == "__main__":
    main()