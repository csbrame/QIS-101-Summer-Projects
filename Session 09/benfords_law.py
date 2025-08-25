#!/usr/bin/env python3
"""benfords_law.py"""

import collections
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot(ax):
    # Set this up by generating 100,000 random numbers
    n = 100000
    # Discreet uniform distribution, from 1 to 1,000,000 inclusive,
    # Then raised to the power of 100.
    random_numbers = (
        np.array([np.random.randint(1, 1_000_001) for _ in range(n)], dtype=object)
        ** 100
    )

    # To find the most significant digit, convert each number to a
    # string and take the first character
    msd_list = [a[0] for a in random_numbers.astype(str)]

    # recast that list of first characters into integers
    msd_array = np.array(msd_list, dtype=int)

    # Create a bin for plotting the counts of each integer
    msd_count = np.zeros(9)
    # Use Counter to get a dictionary for counts of each msd
    for msd, count in collections.Counter(msd_array).items():
        # Index to -1 because our key is offset by one
        # from numpy indexing
        # take the proportion with the total number of msd's
        msd_count[msd - 1] = count / len(msd_array)

    # plot the bars of the histogram and label axis
    plt.bar(np.arange(1, 10), msd_count)
    ax.set_xlabel("Most Significant Digit")
    ax.set_ylabel("Proportion of All Digits")
    ax.set_title("Anomalous Numbers")


def main():
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()


