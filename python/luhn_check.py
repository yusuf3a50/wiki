#!/usr/bin/env python3
"""
Luhn Algorithm Validator
Usage: python luhn_check.py "1234567890"
"""
import sys

def luhn_check(number_string):
    """
    Validate a number string using the Luhn algorithm.
    
    Args:
        number_string: String of digits to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # Remove any spaces or non-digit characters
    digits = [int(d) for d in number_string if d.isdigit()]
    
    if len(digits) == 0:
        return False
    
    # Luhn algorithm implementation
    checksum = 0
    
    # Process digits from right to left
    for i, digit in enumerate(reversed(digits)):
        # Double every second digit (from right)
        if i % 2 == 1:
            digit *= 2
            # If doubled digit > 9, subtract 9 (equivalent to summing digits)
            if digit > 9:
                digit -= 9
        checksum += digit
    
    # Valid if checksum is divisible by 10
    return checksum % 10 == 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python luhn_check.py \"number\"")
        sys.exit(1)
    
    number = sys.argv[1]
    is_valid = luhn_check(number)
    
    # Output with emoji
    emoji = "✅" if is_valid else "❌"
    status = "passes" if is_valid else "fails"
    
    print(f'"{number}" {status} the Luhn algorithm {emoji}')
    
    # Exit with appropriate code
    sys.exit(0 if is_valid else 1)