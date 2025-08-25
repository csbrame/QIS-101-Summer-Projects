#!/usr/bin/env python3
"""eulers_constant.py"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate


def little_gamma(x):
    # This is the integrand to form euler's constant
    return -math.log(math.log(1 / x))


def plot(ax):
    # Perform integration to calculate euler's constant
    eulers_constant = scipy.integrate.quad(little_gamma, 0, 1)[0]
    # Form x, then calculate y
    x = np.linspace(1, 50, 100)
    y = eulers_constant + np.log(x)
    # Typeset a label in LaTeX
    plt.plot(x, y, label=r"$y = \gamma + ln(x)$")

    # create an array of the first 50 natural numbers
    x_harmonic = np.arange(1, 51)
    # Take the cumulative sum of the harmonic terms
    y_harmonic = np.cumsum(1 / np.arange(1, 51))
    # Plot with high z order to overlay the original function
    plt.step(x_harmonic, y_harmonic, zorder=3, label="Harmonic Numbers")
    # Set axis labels, title, and legend
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Euler's Constant and the Harmonic Numbers")
    ax.legend(loc="upper left")


def main():
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
