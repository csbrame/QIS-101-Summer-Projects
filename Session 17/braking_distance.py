#!/usr/bin/env python3
"""braking_distance.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def fit_quadratic(x, y):
    # I'm bringing in fit_quadratic() from quadratic_regression_sklearn.py
    # The motivation for this is modelling the braking car using
    # Newtonian kinematics with constant acceleration due to friction.
    # Our data is in (speed, distance) pairs, not (time, distance),
    # so model distance travelled as d = - 1/(2a) v^2/a

    # Turn the 1D array into a 2D object
    x = x[:, np.newaxis]
    # Specifying degree 2 on PolynomialFeatures for quadratic
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(x)
    # The matrix x2 will have two columns:
    # 1) the original x values and 2) the x**2 values
    x2 = np.array(transformer.transform(x))
    # In order for the linear regression algorith to work, we need as many columns
    # as the degree of the equation we want fitted
    model = LinearRegression().fit(x2, y)
    # Note the .coef_ call vs the .intercept_ call
    a = model.coef_[1]
    b = model.coef_[0]
    c = model.intercept_
    return a, b, c


def main():
    # Import the data from the first road
    file_name = "road1.csv"
    file_path = Path(__file__).parent / file_name
    speed_one, distance_one = np.genfromtxt(file_path, delimiter=",", unpack=True)

    # Import data from second road
    file_name = "road2.csv"
    file_path = Path(__file__).parent / file_name
    speed_two, distance_two = np.genfromtxt(file_path, delimiter=",", unpack=True)

    # Speed is specified as km/h, so convert to m/s using 1000 m/km and 3600 sec/hr
    speed_one, speed_two = (speed_one * 1000 / 3600, speed_two * 1000 / 3600)

    # Scatter the datapoints
    plt.figure(Path(__file__).name, figsize=(10, 8))
    plt.scatter(speed_one, distance_one, zorder=2)
    plt.scatter(speed_two, distance_two, zorder=2)

    # Build a linspace in x with 50 entries along our independent variable
    x = np.linspace(np.min(speed_one), np.max(speed_one))
    # Then do the quadratic fit and plot
    a_one, b, c = fit_quadratic(speed_one, distance_one)
    plt.plot(x, a_one * x**2 + b * x + c, label="Road One", c="r")

    # Do the same thing for road two
    x = np.linspace(np.min(speed_two), np.max(speed_two))
    a_two, b, c = fit_quadratic(speed_two, distance_two)
    plt.plot(x, a_two * x**2 + b * x + c, label="Road Two", c="blue")

    # I'm using the formatting code from quadratic_regression_sklearn.py as well
    plt.title(
        (
            "Braking Distance as a Function of Speed\n"  # noqa
            # Note that the coefficient of the squared term encodes the acceleration
            # on each road, which obeys a = mu * g where mu is the coefficient
            # of friction for each road, as derived by f = mu * N where N = mg
            rf"({a_one / a_two:1.4f} = Average Ratio of $\frac{{\mu_2}}{{\mu_2}}$)"
        )
    )
    plt.xlabel("Speed (m/s)")
    plt.ylabel("Braking Distance (m)")
    plt.grid("on")
    plt.legend(loc="upper left", framealpha=1.0, facecolor="white")
    plt.show()


if __name__ == "__main__":
    main()
