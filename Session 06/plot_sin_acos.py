#!/usr/bin/env python3
"""plot_sin_acos.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot(ax):
    # Get 100 x values on the domain [-1,1], then evaluate
    # y_1(x) and y_2(x) at each point
    x = np.linspace(-1, 1, 100)
    y_1 = np.sin(np.arccos(x))
    y_2 = -1 * np.sqrt(1 - x**2)

    # Get 36 points of theta on the domain [0, 2pi].
    # Then convert to cartesian, recall r=1 on unit circle
    # So r*cos(theta) = cos(theta)
    theta = np.linspace(0, 2 * np.pi, 36)
    x_convert = np.cos(theta)
    y_convert = np.sin(theta)

    # Plot y_1(x) and y_2(x), and then scatter our 36
    # points lying on the unit circle in black color
    ax.plot(x, y_1, label=r"$y=sin(cos^{-1}(x))$")
    ax.plot(x, y_2, label=r"$y=-\sqrt{1-x^2}$")
    ax.scatter(x_convert, y_convert, color="black", label="Unit Circle")

    # Show a legend and label axis
    ax.legend(loc="upper right")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_aspect("equal")


def main() -> None:
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
