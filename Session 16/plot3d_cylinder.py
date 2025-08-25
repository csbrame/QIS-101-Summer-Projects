#!/usr/bin/env python3
"""plot3d_cylinder_.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# declare radius and height
radius, height = 10, 50

u = np.linspace(0, height, 30)  # Vertical location
v = np.linspace(0, 2 * np.pi, 30)  # Horizontal circular slice

# In cylindrical coordinates, x=rcos(theta), y=rsin(theta), z=z
# To accomplish that here, we're going to take the outer products
# using vectors of scalars (radius for x,y, 1 for z)
x = np.outer(radius * np.ones_like(v), np.cos(v))
y = np.outer(radius * np.ones_like(v), np.sin(v))
z = np.outer(u, np.ones_like(v))

# Then we're going to do a surface plot and set the color to red
plt.figure(Path(__file__).name)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z, color="red")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim(-height, height)
ax.set_ylim(-height, height)
ax.set_zlim(0, height)
plt.show()
