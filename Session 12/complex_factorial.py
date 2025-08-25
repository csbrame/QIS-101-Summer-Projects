#!/usr/bin/env python3
"""complex_factorial.py"""

import numpy as np
from scipy.integrate import quad

# Gamma(n) = (n-1)! -> i! = Gamma(i+1)


def integrand(t):
    return (np.cos(np.log(t)) + 1j * np.sin(np.log(t))) * np.e**-t


def main():
    i_factorial = quad(integrand, 0, np.inf, complex_func=True)
    print("i! as calculated from the Gamma function: ", end="")
    print(f"{i_factorial[0]:.8}")


if __name__ == "__main__":
    main()
