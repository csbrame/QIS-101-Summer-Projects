#!/usr/bin/env python3
"""sum_squares.py"""

import numpy as np


def main() -> None:
    """Define the main function, set it to return None."""
    # Create an array of natural numbers from 1-1000 in steps of 1
    natural_numbers = np.arange(1, 1001, 1)
    # Square each element using vectorized squaring operator
    squares = natural_numbers**2
    # Print the sum formatted with commas for thousands
    print("The sum of the squares of the first 1000 natural", end=" ")
    print(f"numbers is {np.sum(squares):,}")

    # Evaluate the Gaussian Functional Equation for n=1000
    # Set type to int instead of float
    gaussian_sum = int((2 * 1000**3 + 3 * 1000**2 + 1000) / 6)
    # Print the result of the Gaussian function equation evaluation
    print("The sum as verified by Gauss' functional", end=" ")
    print(f"equation is {gaussian_sum:,}")


if __name__ == "__main__":
    main()
