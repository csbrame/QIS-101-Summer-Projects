#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

import numpy as np


# Start by defining the Rydberg formula with some simple
# vectorized operations
def rydberg_formula(n_prime, n_naughts):
    reciprocal = 1.09677e7 * (1 / n_prime**2 - 1 / np.power(n_naughts, 2))
    # watch the units, make sure to give final answer in nanometers
    return (1 / reciprocal) * 1e9


# Repeat for bohr's formula
def bohr_formula(n_prime, n_naughts):
    e_naught = (1.602e-19) ** 4 * 9.109e-31 / (8 * 8.854e-12**2 * 6.626e-34**2)
    return (
        1e9
        * 6.626e-34
        * 2.998e8
        / (-1 * e_naught / np.power(n_naughts, 2) + e_naught / n_prime**2)
    )


def main():
    # Establish the pfund and humphreys series from wikipedia.
    # I'm calling 100000 close enough to infinity for an atomic transition
    # We call n=15 high for Rydberg atoms
    pfund_ryd = rydberg_formula(5, np.array([6, 7, 8, 9, 10, 100000]))
    humphreys_ryd = rydberg_formula(6, np.array([7, 8, 9, 10, 11, 100000]))
    # print the results using rydberg formula
    print("From Rydberg formula:")
    print(f"Pfund series, wavelength in nanometers: \n {pfund_ryd.astype(int)}")
    print(
        f"Humphrey's series, wavelength in nanometers: \n {humphreys_ryd.astype(int)}"
    )

    # Repeat for bohr
    pfund_bohr = bohr_formula(5, np.array([6, 7, 8, 9, 10, 100000]))
    humphreys_bohr = bohr_formula(6, np.array([7, 8, 9, 10, 11, 100000]))
    print("From Bohr formula:")
    print(f"Pfund series, wavelength in nanometers: \n {pfund_bohr.astype(int)}")
    print(
        f"Humphrey's series, wavelength in nanometers: \n {humphreys_bohr.astype(int)}"
    )


if __name__ == "__main__":
    main()
