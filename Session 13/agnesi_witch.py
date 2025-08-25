#!/usr/bin/env python3
"""agnesi_witch.py"""

from math import pow
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
from sympy import Poly, lambdify, symbols


def agnesi_witch(a):
    # Define the simplified agnesi witch function with a = 1/2
    return 1 / (np.power(a, 2) + 1)


# For the power series, I'm going to use Dr. Biersach's code from the
# newton_binomial.py script
def calc_coeff(a: float, b: float, r: float, n: int) -> float:
    """
    Returns the coefficient for the (n)th term in the Binomial expansion of (a+b)^r
    """
    coeff = 1.0
    # This for loop is essentially building the factorial for each term
    for m in range(n):
        coeff = coeff * (r - m) / (m + 1)
    coeff = coeff * pow(a, r - n)
    coeff = coeff * pow(b, n)
    return coeff


def binomial_expand(
    a: float, b: float, c: float, r: float, max_t: int
) -> tuple[Poly, Callable[[NDArray[np.float64]], NDArray[np.float64]]]:
    """
    Returns a tuple containing the Binomial Expansion of (a+b*x^c)^r
    to (max_t) terms as a Sympy Polynomial in x, along with
    a callable Numpy expression for that expansion
    """
    # Note that the agnesi witch function can be represented
    # as (1+1*x^2)^-1, giving a=1, b=1, c=2, r=-1
    x = symbols("x")
    poly = 0.0
    for t in range(max_t):
        # Append this term (as a symbolic expression in x)
        # to the growing polynomial of max_t terms
        poly += calc_coeff(a, b, r, t) * x ** (c * t)
    return poly, lambdify(x, poly.as_expr(), modules="numpy")


def main():
    agnesi_domain = np.linspace(-1.499, 1.499, 100)
    # power_domain = np.linspace(-0.999, 0.999, 100)

    plt.figure(Path(__file__).name)
    plt.plot(agnesi_domain, agnesi_witch(agnesi_domain), label="Exact")

    # Once again, I'm going to borrow Dr. Biersach's code from
    # newton_binomial.py to evaluate the series at different numbers
    # of terms
    for t in range(2, 8):
        eqn = binomial_expand(1, 1, 2, -1, t)
        # Evaluate the symbolic expression across the domain x=(-1, 1)
        # map(eqn, x) maps the equation onto every value in power_domain, much like
        # a for loop.
        # Then we're passing that into a list constructor, and
        # turning that into an array
        plt.plot(
            agnesi_domain,
            np.array(list(map(eqn[1], agnesi_domain))),
            label=f"{t} terms",
        )

    # Now just liven up the plot a little bit
    plt.axvline(x=-1, linestyle="dotted", color="black")
    plt.axvline(x=1, linestyle="dotted", color="black")

    ax = plt.gca()
    ax.set_ylim(-2, 2)
    ax.set_title("Runge's Phenomenon (Witch of Agnesi)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="lower center")
    ax.grid("on")
    plt.show()


if __name__ == "__main__":
    main()


"""If we were to include complex numbers, the witch function would
approach infinity around i and 1/2 around -i, giving divergent behavior at
one endpoint of the interval. That would be very bad for the power series.

The witch of agnesi quickly diverges as a power series approximation
as we approach x=-1 or x=1 because the binomial expansion is a
geometric series in x^2. Once x^2 goes beyond 1, the higher order terms get
very large, meaning the series diverges.

Runge's phenomenon says that points on the edge of an interval experience
larger amounts of error/oscillations when doing polynomial approximation
as compared to points in the middle, especially when using evenly spaced
points. Our witch function demonstrates that becasue it diverges alternating
between positive and negative infinity at the edge of the interval."""

