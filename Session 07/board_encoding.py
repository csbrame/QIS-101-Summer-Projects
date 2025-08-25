#!/usr/bin/env python3
"""board_encoding.py"""

import numpy as np


def decode_board(encoding: int):
    # My first idea to decode the function using the modulus
    # approach. I then realized I was just doing base conversion
    # the long way and could use numpy
    # Make a list holding the owner of each space
    space_owners = []
    # Start counting
    count = 0
    while count < 9:
        # Take the modulus of the encoding by 3^count+1, then divide by 3^count
        # This gives the digit 0-2 that is attached to each power of three
        space_owners.append((encoding % 3 ** (count + 1)) // 3**count)
        # Subtract that from the encoding
        encoding -= 3**count * space_owners[-1]
        # Increase the count
        count += 1
    print(space_owners)


def decode_fast(encoding: int):
    # We can go so much faster just using numpy to convert to
    # base three and build a list
    space_owners = list(np.base_repr(encoding, base=3))
    # The list doesn't contain the leading zeroes, so make
    # sure that we form a whole board
    while len(space_owners) < 9:
        space_owners.insert(0, "0")
    # Reverse the list of space_owners to place the MSB at the end
    space_owners = space_owners[::-1]
    # Print the board decoded from the integer
    print(f"Board Encoded by {encoding}:")
    # Just using slicing index for speed
    for n in range(1, 4):
        print(space_owners[3 * (n - 1) : 3 * n])


def main():
    decode_fast(2271)
    decode_fast(1638)
    decode_fast(12065)


if __name__ == "__main__":
    main()
