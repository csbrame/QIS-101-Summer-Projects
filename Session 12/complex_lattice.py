#!/usr/bin/env python3
"""complex_lattice.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def complex_function(z):
    # define our complex function for a single complex input
    return z**2 + z * 1j + 1


def calculate_gaussian_integers():
    # Create arrays of x and y integers
    x = np.arange(-10, 11)
    y = np.arange(-10, 11)
    # Create an array to count how many gaussian integers we find
    count = np.array([])
    # For each integer in x, find how many values of y will satisfy
    # both inequalities derived in the powerpoint
    for i in x:
        # Using boolean indexing to check where the inequalities are satisfied
        mask = np.abs(i**2 - y**2 - y - 1) <= 10
        y_copy = y[mask]
        mask = np.abs(2 * i * y_copy + i) <= 10
        # Append the count of how many gaussian integers we find
        count = np.append(count, len(y_copy[mask]))
    # Print out the final number
    print("The number of Gaussian Integers, such that the magnitudes ", end="")
    print("of |Re(f(x))| and |Im(f(x))| are less than or equal ", end="")
    print(f"to 10 for a Gaussian Integer x, is {int(sum(count))}.")


def plot(ax):
    # Scattering the values
    # First, vectorize the function we built at the start
    f = np.vectorize(complex_function)

    # To generate complex numbers within the proper real and imaginary component
    # domains, use np.random.uniform
    # I found this trick on stackexchange
    complex_numbers = np.random.uniform(-4, 4, 3000) + 1j * np.random.uniform(
        0, 2, 3000
    )

    # Pass that array of complex numbers into our vectorized function
    function_output = f(complex_numbers)

    # Scatter the real and imaginary parts of the starting data
    plt.scatter(
        complex_numbers.real, complex_numbers.imag, color="orange", s=10, zorder=2
    )
    # Scatter the real and imaginary parts of the data after function is applied
    plt.scatter(function_output.real, function_output.imag, color="blue", s=10)
    # Set the title, axis labels, aspect, and grid
    ax.set_title(r"f(z) = z^2 + iz + 1")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_aspect("equal")
    ax.grid("on")


def main():
    # Run the calculatiion
    calculate_gaussian_integers()
    # Plot the scatter
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
