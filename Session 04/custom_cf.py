#!/usr/bin/env python3
"""custom_cf.py"""

import numpy as np


def encode_cf(x):
    """Encode a given number as a cf with 7 terms. Takes as input
    a floating point number or integer. Returns as output the standard
    cf up to 7 terms in the form of a list."""
    cf: list[int] = []
    while len(cf) < 7:  # set max terms
        # Floor x and put it in the cf
        cf.append(int(x))
        # Subtract the floor from the original value
        x = x - int(x)
        # If the difference is zero, we're done
        if x < 1e-11:
            break
        # Set x as the reciprocal of the difference
        x = 1 / x
    # "Normalize" the continued fraction
    if cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1
        cf.pop(-1)
    return cf


def main() -> None:
    # Create a numpy array with natural numbers 1-9
    naturals_array = np.array(range(1, 10))
    # Apply the given x_n function to all elements of the array
    real_array = (
        1 + np.sqrt(4 * np.power(naturals_array, 2) - 4 * naturals_array + 5)
    ) / 2
    for i in range(0, 9):
        # Print the original value and the cf for every element
        print("The standard continued fraction to seven terms for ", end="")
        print(f"{real_array[i]} is {encode_cf(real_array[i])}.")


if __name__ == "__main__":
    main()

#########################################
# Line 34 should contain range(1,10) just like your real array
# We still want to print the standard continued fraction for x_1 through x_9.
# You should also rename the real_array variable since you use it twice for first creating
# the array, and then using it for the function.
# The code is right, you just need to change the range and fix the variable!

# Hi Jane! I renamed the original arange array to avoid the redundancy
# and then changed the range for the print to (0, 9). (1,10) gave me
# an indexing error there due to index nine being offset by 1.
