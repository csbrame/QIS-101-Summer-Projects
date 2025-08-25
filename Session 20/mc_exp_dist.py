#!/urs/bin/env python3
"""mc_exp_dist.py"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from numba import float64, int64, vectorize
from numpy import ndarray

# Declare the Rate Parameter for the exponential distribution pdf
# I'm using units of hours, that way 60 minutes becomes 1 hr, meaning
# our integral is only up to x=1
RATE_PARAMETER = 1.5


@vectorize([float64(int64, int64)], nopython=True)
def halton(n, p):
    # Start by defining the halton method for random number generation
    # Using numba to speed it up, this is just code from Dr. Biersach
    # specifically from mc_std_normal.ipynb
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


def exp_pdf(x: ndarray):
    # PDF of the exponential distribution, describing a poisson process
    return RATE_PARAMETER * np.exp(-RATE_PARAMETER * x)


def main():
    # Define the rectangle
    # Anchor point at (0,0), since the pdf = 0 for x<=0
    # Width of 1, since we want x to run from 0-1 hr
    # Then height of 1.75 so that we capture the whole pdf
    # We choose height of 1.75 because the rate_parameter is 1.5, and pdf(0)=1.5
    # is a maximum
    bbox = Rectangle((0, 0), 1, 1.75).get_bbox()

    # Set our total number of dots to 25,000
    total_dots = 25_000

    # Generate 25,000 random points using halton method
    x = (1 - halton(np.arange(total_dots), 2)) * bbox.width + bbox.x0
    y = (1 - halton(np.arange(total_dots), 3)) * bbox.height + bbox.y0

    # Let d be the difference of the y coordinate of each random point
    # and the pdf at that x value
    # any point with d>0 is above the pdf, anything d<=0 is on or below
    d = y - exp_pdf(x)

    # Use boolean indexing to get separate the points inside from outside
    x_in = x[d <= 0.0]
    y_in = y[d <= 0.0]
    x_out = x[d > 0.0]
    y_out = y[d > 0.0]

    # Get our estimate for the CDF evaluated at x=1hr:
    est = (bbox.width * bbox.height) * np.count_nonzero(d <= 0) / total_dots

    # The analytic solution is 1-e^(-lambda x) = 1-e^(-1.5) in our case
    # To get that, we just take the integral of the pdf up to x
    act = np.round(1 - np.exp(-1.5), 5)

    # Get the error in our estimate and print to the console
    err = np.abs((est - act) / act)

    print(f"dots = {total_dots:,}")
    print(f"Actual Probability = {act:.6f}")
    print(f"Estimated Probability = {est:.6f}")
    print(f"Error = {err:.5%}")

    # Plot the analytic form of the pdf, scatter the randomly generated
    # points, colorcoded as above or below the curve
    # This plotting code comes right from mc_std_normal.ipynb
    pdf_x = np.linspace(0, 4, 100)
    pdf_y = exp_pdf(pdf_x)

    plt.figure(figsize=(10, 8))
    plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
    plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
    plt.plot(
        pdf_x,
        pdf_y,
        color="green",
        label=r"$\lambda e^{-\lambda x}$",
    )
    plt.title("Exponential Distribution CDF")
    plt.axhline(0, color="gray")
    plt.axvline(0, color="gray")
    plt.xlim(-0.5, 3)
    plt.ylim(-0.1, 2)
    plt.xlabel("x")
    plt.ylabel("PDF")
    plt.legend(loc="upper right", fontsize="12")
    plt.show()


if __name__ == "__main__":
    main()
