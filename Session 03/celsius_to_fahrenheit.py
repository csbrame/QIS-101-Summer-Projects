#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""

import numpy as np


def main() -> None:
    """Define the main function and specify it returns None, simply executes what's inside."""
    # Create an array with elements from -44 to 104 in steps of 4 for celsius temperatures
    celsius = np.arange(-44, 105, 4)
    # Perform vectorized scalar multiplication and addition to create an array of fahrenheit data from the celsius array
    fahrenheit = (9 / 5) * celsius + 32
    # Print out the data in pairs of entries using a for loop
    for i in range(len(celsius)):
        # Print using a formatted string and specify for the numbers: right justification, 6 digits, 2 after the decimal, fixed
        print(f"{celsius[i]:>6.2f} C = {fahrenheit[i]:>6.2f} F")


# Execute main()
if __name__ == "__main__":
    main()
