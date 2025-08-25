#!/usr/bin/env python3
"""doppler_redshift.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# Start by defining the Rydberg formula with some simple
# vectorized operations. I'm pulling this right from task 08-01
def rydberg_formula(n_prime: int, n_naughts: np.ndarray):
    reciprocal = 1.09677e7 * (1 / n_prime**2 - 1 / np.power(n_naughts, 2))
    # watch the units, make sure to give final answer in nanometers
    return (1 / reciprocal) * 1e9


def relativistic_correction(speed: int, transitions: np.ndarray):
    # for the relativistic doppler effect, assumer speed is some
    # number from 0-1 representing the ratio of velocity to the
    # speed of light (exactly Beta)
    # Recall the wavelength at the receiver is the wavelength
    # from the source multiplied by the square root of a ratio
    return transitions * np.sqrt((1 + speed) / (1 - speed))


def plot(ax):
    # Balmer series has final energy level n=2
    n_final = 2
    # We're going to use an ndarray to set our starting energy levels
    # once again, 100000 more than high enough
    n_starts = np.array([3, 4, 5, 6, 7, 100000])

    # Starting with stationary hydrogen atom
    balmer_stationary = rydberg_formula(n_final, n_starts)
    # We then plot using axv lines
    for a in balmer_stationary:
        if a == balmer_stationary[0]:
            plt.axvline(x=a, color="blue", label="Stationary")
        else:
            plt.axvline(x=a, color="blue")
    # Repeat for 10% of speed of light
    # Recall we're passing beta in directly as the speed proportion
    balmer_10 = relativistic_correction(0.1, balmer_stationary)
    for a in balmer_10:
        if a == balmer_10[0]:
            plt.axvline(x=a, color="green", label="10% Speed of Light")
        else:
            plt.axvline(x=a, color="green")
    # Next 30%
    balmer_30 = relativistic_correction(0.3, balmer_stationary)
    for a in balmer_30:
        if a == balmer_30[0]:
            plt.axvline(x=a, color="orange", label="30% Speed of Light")
        else:
            plt.axvline(x=a, color="orange")
    # Next 50%
    balmer_50 = relativistic_correction(0.5, balmer_stationary)
    for a in balmer_50:
        if a == balmer_50[0]:
            plt.axvline(x=a, color="pink", label="50% Speed of Light")
        else:
            plt.axvline(x=a, color="pink")
    # Finally 80%
    balmer_80 = relativistic_correction(0.8, balmer_stationary)
    for a in balmer_80:
        if a == balmer_80[0]:
            plt.axvline(x=a, color="red", label="80% Speed of Light")
        else:
            plt.axvline(x=a, color="red")

    # Set the x axis label, we don't have a y-axis unit
    ax.set_xlabel(r"$\lambda$ Wavelength in nm")
    ax.set_title("Balmer Series and Relativistic Corrections")
    ax.legend(loc="upper right")


def main():
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
