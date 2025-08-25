#!/usr/bin/env python3
"""plot_limits.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot(ax_1, ax_2):
    # Create an array with an odd number of x values
    # with x from [-1,1]
    x = np.linspace(-1, 1, 89)
    # Apply functions y_1 and y_2
    y_1 = 12 * (x - np.sin(x)) / x**3
    y_2 = (np.exp(x) - np.exp(-x) - 2) / (x - np.sin(x))

    # Take the middle 5 entries from each array and format
    # them to print as f strings
    # This intermediate step was the only way I could find to do
    # this f string work with numpy arrays
    slice_one = y_1[(len(y_1) // 2 - 2) : (len(y_1) // 2 + 3)]
    formatted_y_1_slice = [f"{a:.4f}" for a in slice_one]
    slice_two = y_2[(len(y_2) // 2 - 2) : (len(y_2) // 2 + 3)]
    formatted_y_2_slice = [f"{a:,.2f}" for a in slice_two]

    # Plot the data on two different subplots in the same
    # figure, since their scales are so different
    # Put an empty dot at where the limit disappears for y_1
    ax_1.plot(x, y_1, label=r"$y_1=12(\frac{x-sin(x)}{x^3})$")
    ax_1.scatter(0, 2, facecolors="none", edgecolors="red")
    ax_2.plot(x, y_2, label=r"$y_2=\frac{e^x-e^{-x}-2}{x-sin(x)}$")

    # Style up the plots a little bit
    ax_1.set_xlabel("$x$")
    ax_1.set_ylabel("$y_1$")
    ax_1.axis("on")
    ax_1.grid("on")

    ax_2.set_xlabel("$x$")
    ax_2.set_ylabel("$y_2$")
    ax_2.axis("on")
    ax_2.grid("on")

    # Print the formatted center 5 entries from each array
    print("The middle five values for y_1: ", end="")
    print(f"{formatted_y_1_slice}")
    print("The middle five values for y_2: ", end="")
    print(f"{formatted_y_2_slice}")


def main() -> None:
    plt.figure(Path(__file__).name)
    # Get the plot to come up fullscreen right away
    plt.get_current_fig_manager().full_screen_toggle()
    # Pass two axes objects into plot, one for each subplot
    plot(plt.subplot(121), plt.subplot(122))
    plt.show()


if __name__ == "__main__":
    main()
