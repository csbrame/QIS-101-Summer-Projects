#!/usr/bin/env python3
"""lead_attenuation.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


def percent_photons(mu_value, distance):
    # Simple way to return the percent of photons for a given
    # attenuation coefficient and path length
    return 100 * np.exp(-mu_value * distance)


def main():
    # Start by forming the path and append the file name
    file_path = Path(__file__).parent / "lead_attenuation.csv"
    # Read it out with numpy into two arrays
    energy, mu_energy = np.genfromtxt(file_path, delimiter=",", unpack=True)

    # Since the data is not sorted out of the file, find the min and max
    min_energy, max_energy = np.min(energy), np.max(energy)
    # Then create an array of 1000 values between the min and max
    # to model the curve
    energy_model = np.linspace(min_energy, max_energy, 1000)

    # Use cubic spline to interpolate a function given our
    # original data
    attenuation_function = CubicSpline(energy, mu_energy)
    # Feed our 1000 points into the interpolated funtion to get out a
    # smooth curve
    attenuation_model = attenuation_function(energy_model)

    # Calculate the attenuation factor for 4.65MeV
    attenuation_465 = attenuation_function(4.65)
    # Give that value and the distance to the percent function
    passing_percent = percent_photons(attenuation_465, 2)
    # Print out calculated results
    print("The attenuation coefficient for photons of 4.65MeV ", end="")
    print(
        "passing through lead, as calculated by our interpolated function, is ", end=""
    )
    print(f"{attenuation_465:.6}.\nThe percent of photons of energy 4.65MeV ", end="")
    print(f"that passes all the way through lead 2cm thick is {passing_percent:.4}%.")

    # Scatter the original data
    plt.scatter(energy, mu_energy)
    # PLot the curve of the interpolated function
    plt.plot(energy_model, attenuation_model, color="black")
    # Set the y scale to log base 10
    plt.yscale("log")
    # Set title, get the current axes, and add some labels
    plt.title("Lead Attenuation Coefficient")
    axes = plt.gca()
    axes.set_xlabel("Energy[MeV]")
    axes.set_ylabel(r"$\mu(cm^{-1})$")
    plt.show()


if __name__ == "__main__":
    main()
