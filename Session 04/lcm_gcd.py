#!/usr/bin/env python3
"""lcd_gcm.py"""

from math import gcd


def get_lcm(a, b):
    """Determining the lcm of 2 integers. Takes a, b as input,
    divides their product by their gcd, and returns the answer."""
    return int(a * b / gcd(a, b))


def main() -> None:
    print("The Least Common Multiple of 447,618 and 2,011,835", end=" ")
    print(f"is {get_lcm(447618, 2011835):,}.")


if __name__ == "__main__":
    main()
