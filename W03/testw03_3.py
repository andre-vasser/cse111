from typing import List

def get_fruit_lengths(fruits: List[str]) -> List[int]:
    """
    Returns a list of lengths of the given fruits.

    Args:
        fruits (List[str]): A list of strings representing fruits.

    Returns:
        List[int]: A list of lengths of the given fruits.
    """
    lengths = [len(fruit) for fruit in fruits]
    return lengths

def print_range_sum(numbers: List[int]) -> None:
    """
    Prints the sum of numbers in the given range.

    Args:
        numbers (List[int]): A list of integers representing the range.
    """
    total = sum(numbers)
    print(f"The sum of numbers in the range is: {total}")

def print_min_max_abs(numbers: List[int]) -> None:
    """
    Prints the minimum, maximum, and absolute values of the given numbers.

    Args:
        numbers (List[int]): A list of integers.
    """
    maximum = max(numbers)
    minimum = min(numbers)
    abs_values = [abs(num) for num in numbers]

    print(f"The maximum number is: {maximum}")
    print(f"The minimum number is: {minimum}")
    print(f"The absolute values are: {abs_values}")

def main() -> None:
    """
    Main function to demonstrate the built-in functions.
    """
    fruits = ["apple", "banana", "cherry"]
    fruit_lengths = get_fruit_lengths(fruits)
    print(f"The lengths of the fruits are: {fruit_lengths}")

    numbers = [1, 2, 3, 4, 5]
    print_range_sum(numbers)

    numbers = [-5, 2, 8, -1, 9]
    print_min_max_abs(numbers)

if __name__ == "__main__":
    main()