#!/usr/bin/env python3
"""archimedes_spiral.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate
from matplotlib.ticker import MultipleLocator


def inftessimal_arc(theta):
    """the integrand of the integral to find the arc length
    of our archimedes spiral"""
    # I found this formula off of wikipedia
    return np.sqrt(theta**2 + 1)


def plot(ax):
    # To plot the spiral, we want to define our theta over the
    # appropriate domain, then convert to cartesian with r=theta
    theta = np.linspace(0, 8 * np.pi, 100)
    x = theta * np.cos(theta)
    y = theta * np.sin(theta)
    plt.plot(x, y)
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.set_title(r"Archimedes Spiral: $r = \theta$")
    ax.set_aspect("equal")


def main():
    # To get the arc length, use scipy to integrate over theta
    arc_length = scipy.integrate.quad(inftessimal_arc, 0, 8 * np.pi)[0]
    # Print the arc length
    print("The arc length calculated by SciPy = ", end="")
    print(f"{arc_length}")
    # Plot the spiral
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
