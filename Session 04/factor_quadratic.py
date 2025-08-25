#!/usr/bin/env python3
"""factor_quadratic.py"""

from math import gcd


def factor_quadratic(J: int, K: int, L: int) -> None:
    """Factor a degree 2 polynomial with positive, integer coefficients
    J, K, L. Take the coefficients as input and return a print of their
    factorization."""
    print("Given the quadratic:", end=" ")
    print(f"{J}x^2 + {K}x + {L}")

    scalar_factor = gcd(J, K, L)
    # Using tuple comprehension, divide out the gcd and save it
    J, K, L = (int(i / scalar_factor) for i in (J, K, L))

    for a in range(1, J + 1):
        # Create a 'found' marker to stop looking once a factorization has been found
        found = False
        # Start looking for integers that divide J.
        if J % a == 0:
            # When we find an a that divides J, set J / a as c.
            c: int = J // a
            # Then start looking for b and d by searching for a divisor of L
            for b in range(1, L + 1):
                if L % b == 0:
                    # When we find a b that divides L, call L / b as d
                    d: int = L // b
                    # Check whether FOIL yields the correct third coefficient
                    if a * d + b * c == K:
                        # If yes, then print the factorization, if no, repeat
                        print("The factors are:", end=" ")
                        # If the gcd is not 1, then show that it was factored out
                        if scalar_factor != 1:
                            print(f"{scalar_factor}({a}x + {b})({c}x + {d})")
                        # Otherwise, just print with leading 1 implied
                        else:
                            print(f"({a}x + {b})({c}x + {d})")
                        # Mark that the factorization was found
                        found = True
        if found:
            break

    """Every degree two polynomial has one unique factorization, but we're 
    only checking positive integer factors. So here's a cop out."""
    if not found:
        print("No factors could be found.")


def main() -> None:
    factor_quadratic(115425, 3254121, 379020)


if __name__ == "__main__":
    main()
