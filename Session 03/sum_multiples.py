#!/usr/bin/env python3
""" "sum_multiples.py"""

import numpy as np


def main() -> None:
    """Define main() to sum the natural numbers less than 1900 satisfying our condition"""
    # Create an array with natural numbers from 1 - 1900, exclusive
    natural_numbers = np.arange(1, 1900, 1)
    """Create another array from those elements which return zero for 
    modulo base 77. Any number that is divisible by both 7 and 11 is divisible
    by 77 and vice versa."""
    satisfiers = natural_numbers[np.where(natural_numbers % 77 == 0)]
    # Print the sum of those numbers collected in the new array.
    print("The sum of the natural numbers less than 1900 that", end=" ")
    print(f"are divisible by both 7 and 11 is {np.sum(satisfiers):,}")


if __name__ == "__main__":
    main()
