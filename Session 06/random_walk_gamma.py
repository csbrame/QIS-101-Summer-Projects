#!/usr/bin/env python3
"""random_walk_gamma"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sympy


def get_expected_distance(dims, max_steps):
    """Returns the expected final distance of a uniform random
    walk of max_steps steps on a unit lattice with dimension d"""
    # Establish symbols to use with sympy, denote z, d, and N as
    # strictly positive. If we don't, sympy gets a piecewise function
    # when it evaluates the integral, and that messes up lambdify
    t = sympy.symbols("t")
    z, d, N = sympy.symbols("z d N", positive=True)
    # Define Euler's Gamma function as a function in z
    euler_gamma = sympy.integrate(t ** (z - 1) * sympy.exp(-t), (t, 0, sympy.oo))
    # Create an expression for the expected distance by substituting
    # (d+1)/2 and d/2 into the gamma function, taking the square of their quotient,
    # and multiplying that by the square root of 2N/d
    expected_distance = (
        sympy.sqrt(2 * N / d)
        * (euler_gamma.subs(z, (d + 1) / 2) / euler_gamma.subs(z, d / 2)) ** 2
    )
    # Pass that expression into sympy.lambdify. Specify that it should
    # be a function of two variables (d, N), and that it should work with
    # numpy (It ends up not working with numpy for me for some reason)
    distance_lambda = sympy.lambdify((d, N), expected_distance, modules="numpy")
    # Return the expected final distance of a walk of N steps on a
    # lattice of dimension d
    return distance_lambda(dims, max_steps)


def plot(ax):
    # Create a numpy array of distance values in the given range
    dimension_array = np.linspace(1, 25, 125)
    # Specify steps of each random walk
    step_count = 20000
    # I tried passing this numpy vector into lambdified function but
    # could not get past an error. Falling back on a for loop
    # The function works properly with integer arguments (I think)
    # and I don't want to spend hours figuring out whatever weirdness
    # is giving sympy trouble
    distances = np.array([])
    for i in dimension_array:
        distances = np.append(distances, get_expected_distance(i, step_count))
    # Plot the expected distance as a function of dimension
    ax.plot(dimension_array, distances)
    ax.set_title(
        "Expected Final Distance of a Uniform Random Walk as a Function of Lattice Dimension"
    )
    ax.set_xlabel("$d$ - Dimension")
    ax.set_ylabel("$E$ - Expected Final Distance")
    ax.grid("on")


def main() -> None:
    plt.figure(Path(__file__).name)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
