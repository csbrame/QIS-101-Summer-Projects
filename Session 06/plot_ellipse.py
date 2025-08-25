#!/usr/bin/env python3

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot(ax):
    # Create an nparray for theta from [0, 2pi) with 200 values
    theta = np.linspace(0, 2 * np.pi, 200)
    # Calculate radius using vectorized operations on the theta array
    # Derive polar equation using x=rcos(theta), y=rsin(theta), and
    # (x/100)^2 + (y/50)^2 = 1 as equation of ellipse
    radius = np.power((np.cos(theta) / 100) ** 2 + (np.sin(theta) / 50) ** 2, -1 / 2)

    # Turn the polar data into cartesian and plot
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    ax.plot(x, y)

    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    # Title the graph with the polar equation, since that is
    # the equation used to generate the points
    ax.set_title(r"$r=(\frac{cos^2(\theta)}{100^2}+\frac{sin^2(\theta)}{50^2})^{-1/2}$")

    ax.set_xlim(x[len(x) // 2] * 1.1, x[0] * 1.1)
    ax.set_ylim(y[len(y) * 3 // 4] * 1.1, y[len(y) * 1 // 4] * 1.1)

    # Set the aspect to be equal to represent the correct proportions
    ax.set_aspect("equal")
    ax.grid("on")


def main():
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
