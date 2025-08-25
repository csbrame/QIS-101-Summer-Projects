#!/usr/bin/env python3
"""ifs_hexagonal.py"""

import numpy as np
from ifs import IteratedFunctionSystem
from pygame import Color
from simple_screen import SimpleScreen

ifs = IteratedFunctionSystem()


def plot_ifs(ss):
    iterations = 200_000
    x, y = 0.0, 0.0

    # Iterate 100 times, but don't draw any pixels
    # This will give the IFS "time" reach its stable orbit
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)


def main():
    # Create a 30x30 base frame, center the haxagon at (15,15)
    # let the hexagon side lengths be 10
    ifs.set_base_frame(0, 0, 30, 30)

    # Get the height of the third point on one of the 6 triangles in
    # the hexagon using tan(60) = h / 5
    h = 5 * np.sqrt(3)

    # Give each transformation an equal probability of occurence
    p = 1 / 6

    # Enter your mappings here

    # COD
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + h, Color("blue"), p)
    # DOE
    ifs.add_mapping(20, 15 + h, 15, 15, 10, 15 + h, Color("blue"), p)
    # EOF
    ifs.add_mapping(10, 15 + h, 15, 15, 5, 15, Color("blue"), p)
    # FOA
    ifs.add_mapping(5, 15, 15, 15, 10, 15 - h, Color("blue"), p)
    # AOB
    ifs.add_mapping(10, 15 - h, 15, 15, 20, 15 - h, Color("blue"), p)
    # BOC
    ifs.add_mapping(20, 15 - h, 15, 15, 25, 15, Color("blue"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Hexagonal",
    )
    ss.show()


if __name__ == "__main__":
    main()
