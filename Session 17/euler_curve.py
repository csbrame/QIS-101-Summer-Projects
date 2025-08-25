#!/usr/bin/env python3
"""euler_curve.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def x_curve(u):
    # Define the parametric curve for x
    return np.cos(u**2)


def y_curve(u):
    # Define the parametric curve for y
    return np.sin(u**2)


def arc_length(t_i, t_f):
    # Note, the arc length of a parametric curve is given as
    # integral(a, b)[dx/dt and dy/dt summed in quadrature]dt
    # Taking the derivative of x with respect to t removes the integral
    # and evaluates the function at t, meaning dx/dt = cos(t ** 2)
    # Thus, dy/dt = sin(t ** 2)
    # The sum of the squares of those derivatives is 1, so
    # the arc length is given by integral(a, b)[1]dt = b - a
    return t_f - t_i


def main():
    # Create a linspace for t with the default 50 values, exclude the endpoint
    t = np.linspace(0, 12.34, 1000, endpoint=False)

    # Create arrays to hold x and y values
    x = np.zeros_like(t)
    y = np.zeros_like(t)

    # Evaluate the parametric equations at each timestep
    for i in range(len(t)):
        x[i] = quad(x_curve, 0, t[i])[0]
        y[i] = quad(y_curve, 0, t[i])[0]

    plt.figure(Path(__file__).name, figsize=(10, 8))
    plt.plot(x, y)

    # I had a lot of trouble with the integral diverging in scipy, so I
    # researched the integrals online and found they are called the
    # Fresnel Integrals and they converge as t->infinity
    # That convergence point is sqrt(2pi) / 4, so I'm scattering that
    plt.scatter(np.sqrt(2 * np.pi) / 4, np.sqrt(2 * np.pi) / 4, color="red")

    # I'm going to include the arc length of the curve in the title portion
    plt.title(
        (
            "Parametric Curves\n"  # noqa
            rf"Arc Length up to $t=12.34$: {arc_length(0, t[-1])}"
        )
    )
    # And labeling the x and y axes with the parametric equations
    plt.xlabel(r"$x(t)=\int_{0}^{t} cos(u^2) \,du\ $")
    plt.ylabel(r"$y(t)=\int_{0}^{t} sin(u^2) \,du\ $")
    plt.show()


if __name__ == "__main__":
    main()
