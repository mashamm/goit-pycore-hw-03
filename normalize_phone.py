import re

def normalize_phone(phone_number):
    """
    Normalize phone number to international format.

    Args:
        phone_number: String with phone number in various formats.

    Returns:
        str: Normalized phone number (+380 + 9 digits), or "" if invalid length.
    """
    cleaned = re.sub(r"[^\d+]", "", phone_number)
    digits = cleaned.lstrip("+")
    if digits.startswith("380"):
        result = "+" + digits
    else:
        result = "+38" + digits
    if len(result) != 13:  # +380 + 9 digits = 13 chars
        return ""
    return result


def main():
    raw_numbers = input("Enter phone numbers (comma-separated): ").split(",")
    sanitized = [n for num in raw_numbers if (n := normalize_phone(num.strip()))]
    print("Нормалізовані номери:", sanitized)

if __name__ == "__main__":
    main()