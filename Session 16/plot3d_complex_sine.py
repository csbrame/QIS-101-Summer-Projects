#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator


def f(z):
    # Define the sine function
    return np.abs(np.sin(z))


def main():
    # Create two arrays, one for the domain of the real
    # components, one for the domain of the imaginary
    real_coords = np.linspace(-2.5, 2.5, 50)
    imag_coords = np.linspace(-1, 1, 50)

    # Use mashgrid to create a grid of points, not just a line
    # Return the x and y vectors that represent point pairs
    x, y = np.meshgrid(real_coords, imag_coords)

    # Vectorize the complex function to turn pass in ndarrays
    complex_vec = np.vectorize(complex)

    # Calculate the sine function using our defined f(z)
    # Note that we use the vectorized complex function to
    # pass in the complex argument
    z = f(complex_vec(x, y))

    # Create the figure
    plt.figure(Path(__file__).name, figsize=(8, 4))
    # Get the 3D axes
    ax = plt.axes(projection="3d")

    # I'm using the same name and code mostly as the surface in
    # plot3D_surface.py
    surf = ax.plot_surface(x, y, z, cmap="coolwarm", lw=0, antialiased=False)
    # Make a colorbar to help visualize what the cool warm colors mean
    plt.colorbar(surf, ax=ax, shrink=0.5)

    # Set some tick marks along the z axis, format their decimal places
    # and then label and show
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()


if __name__ == "__main__":
    main()
