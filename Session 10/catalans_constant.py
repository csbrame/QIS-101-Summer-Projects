#!/usr/bin/env python3
"""catalans_constant.py"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate


def log_integrand(x):
    # A simple function to represent the integrand
    # Note that it is made to take ndarrays, since we want to plot it
    return np.log(np.sin(x) + np.cos(x))


def main():
    # Start with an array of natural numbers beginning at 0
    naturals = np.arange(0, 400)
    # Perform array operations to turn the naturals into the sequence
    # which can be summed to give catalan's constant
    sum_terms = (-1) ** naturals / (2 * naturals + 1) ** 2
    # Sum the entries of the matrix to get catalan's constant
    # round off at 15 decimal places. That's 15 significant digits,
    # since the value is less than 1
    catalan_constant = round(sum(sum_terms), 15)

    # Find the value of the specified difference to 15 decimal places
    difference_value = round(catalan_constant - (np.pi * np.log(2)) / 4, 15)
    # Print the value of the difference
    print(rf"The calculated difference = {difference_value}")

    # Take the integral of our function
    integral_estimate = scipy.integrate.quad(log_integrand, 0, np.pi / 2)[0]
    # print the value of the integral
    print(f"The numerical estimate of the integral = {integral_estimate:1.15}")
    # Note that the two values are close, but not exactly equal
    # It's not clear if one bounds the other or if they converge
    # in the limit that we evaluate catalan's constant for n -> inf
    print("The two values are very close, though not necessarily equal.")

    # Create x and y to plot the integrand
    x = np.linspace(0, np.pi / 2, 100)
    y = log_integrand(x)

    # Plot the integrand
    plt.plot(x, y)
    axes = plt.gca()
    axes.set_xlabel("x")
    axes.set_ylabel(r"$ln(sin(x)+cos(x))$")
    axes.set_title("Natural Log of the Sum of Sine and Cosine")
    plt.show()


if __name__ == "__main__":
    main()
