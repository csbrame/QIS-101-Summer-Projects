#!/usr/bin/env python3
"""werner_formula.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Set our x domain from [-3pi,3pi]
x = np.linspace(-3 * np.pi, 3 * np.pi)

# Establish our figure
plt.figure(Path(__file__).name)

# PLot all four functions
plt.plot(x, np.sin(0.8 * x), label=r"$sin(0.8x)$")
plt.plot(x, np.sin(0.5 * x), label=r"$sin(0.5x)$")
plt.plot(x, np.sin(0.8 * x) * np.sin(0.5 * x), label=r"$sin(0.8x) * sin(0.5x)$")
# Make sure to use only grey circle markers
plt.plot(
    x,
    1 / 2 * (np.cos(0.3 * x) - np.cos(1.3 * x)),
    "o",
    label=r"$\frac{1}{2}(cos((0.8-0.5)x) - cos((0.8 + 0.5)x))$",
    color="grey",
    markerfacecolor="none",
)

# Make the plot look nicer
ax = plt.gca()
ax.set_title("Sine Waves of Two Frequencies")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(loc="upper right")
plt.show()
