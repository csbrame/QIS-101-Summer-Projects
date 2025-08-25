#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# Build the PDF of the Maxwell-Boltzmann Distribution to handle
# numpy arrays as input.
# Got my equation from wikipedia
def maxwell_boltzmann_pdf(alpha: int, velocities: np.ndarray):
    return (
        np.sqrt(2 / np.pi)
        * (velocities**2 / alpha**3)
        * np.exp(-(velocities**2) / (2 * alpha**2))
    )


def plot(ax):
    # Get a velocity distribution from [0,20]
    x = np.linspace(0, 20, 500)
    # Calculate the maxwell-boltzmann distribution for 3 values of alpha
    dist_one = maxwell_boltzmann_pdf(1, x)
    dist_two = maxwell_boltzmann_pdf(2, x)
    dist_five = maxwell_boltzmann_pdf(5, x)

    # Plot all three on the same graph
    plt.plot(x, dist_one, label=r"$\alpha = 1$")
    plt.plot(x, dist_two, label=r"$\alpha = 2$")
    plt.plot(x, dist_five, label=r"$\alpha = 5$")

    # Pretty up the graph with labels and a title
    ax.set_xlabel("Velocity")
    ax.set_ylabel("Probability Distribution Function")
    ax.set_title("Maxwell-Boltzmann Distribution for Various Alpha's")
    ax.legend(loc="upper right")


def main():
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
