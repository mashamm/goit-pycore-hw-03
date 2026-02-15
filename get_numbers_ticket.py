import random


def get_numbers_ticket(min_val, max_val, quantity):
    """
    Generate unique random lottery numbers within a specified range.

    Args:
        min_val: Minimum possible number (inclusive), must be >= 1.
        max_val: Maximum possible number (inclusive), must be <= 1000.
        quantity: Number of numbers to select, must be between min and max
                  and not exceed the range size (max_val - min_val + 1).

    Returns:
        list: Sorted list of unique random integers, or empty list if
              parameters are invalid.
    """
    if (
        min_val < 1
        or max_val > 1000
        or min_val > max_val
        or quantity < min_val
        or quantity > max_val
        or quantity > (max_val - min_val + 1)
    ):
        return []
    return sorted(random.sample(range(min_val, max_val + 1), quantity))


def main():
    min_val = int(input("Enter a minimum value: "))
    max_val = int(input("Enter a maximum value: "))
    quantity = int(input("Enter a quantity: "))
    print(get_numbers_ticket(min_val, max_val, quantity))


if __name__ == '__main__':
    main()
