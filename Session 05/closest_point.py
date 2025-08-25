#!/usr/bin/env python3
"""closest_point.py"""

import random
import time
from math import sqrt
from pprint import pprint

import numpy as np


def generate_points(n, x_range, y_range):
    """Generate n random points within the given range."""
    random.seed(2022)
    return [
        (round(random.uniform(*x_range), 4), round(random.uniform(*y_range), 4))
        for _ in range(n)
    ]


def closeness(one, two):
    """Return the distance between two given points"""
    return sqrt((one[0] - two[0])** 2 + (one[1] - two[1])** 2)


def closest_pair(points):
    """Find the Closest Pair quickly. This function takes in a list of tuples,
    then returns the closest pair and their separation in regard to 
    euclidean distance."""
    min_dist = float("inf")
    closest_pair = ((0, 0), (0, 0))
    # Calculate the distance from 0 for each point. Close points have similar distances
    distances_list = [
        sqrt(points[i][0] ** 2 + points[i][1] ** 2) for i in range(0, len(points))
    ]
    # Turn the list into an array
    distances = np.array(distances_list)
    # Get the indices to sort the array
    indices = np.argsort(distances)
    # Place both the distances and their associated points in sorted order
    points_array, distances = np.array(points)[indices], distances[indices]
    # Iterate through the entries of distances, but only one time
    for i in range(len(distances) - 1):
        """Subtract the value from the rest of the array. Since the array is in ascending order,
        the closest distances will be nearly zero, and they should fall just in front
        of the current index."""
        distances = distances - distances[i]
        """If the two are a similar distance from zero, then check the angle between them. 
        If that is small, then check the distance between the two. If that is the closest distance yet,
        then set that pair as closest neighbors. 
        This method has a key flaw. It only looks at adjacent entries in the distance array. I'm 
        assuming that the two closest neighbors will be so close that they are virtually the same, so they
        should be next to each other, but that's not necessarily true. There could be a point at exactly the same
        distance from zero as one of the points, putting it between them on the distance list.
        In the future, I would do a bit of a broader sweep, comparing a few different entries
        based on a closeness criteria, but this is already too complicated for me."""
        if (
            np.abs(distances[i] - distances[i + 1]) < 1e-2
            and (
                np.abs(
                    np.linalg.norm(np.cross(points_array[i], points_array[i + 1]))
                    / (
                        np.linalg.norm(points_array[i])
                        * np.linalg.norm(points_array[i + 1])
                    )
                )
                < 1e-3
            )
            and (closeness(points_array[i], points_array[i + 1]) < min_dist)
        ):
            closest_pair = (points_array[i], points_array[i + 1])
            min_dist = closeness(points_array[i], points_array[i + 1])
    return closest_pair, min_dist


def slow_close_pair(points):
    """This is a method to find the closest pair the slow way, taking the
    distance between every single pair of points and comparing"""
    min_dist = float("inf")
    close_pair = ((0, 0), (0, 0))
    for i in range(len(points)):
        focus_pair = points[i]
        for j in range(len(points)):
            if j == i:
                continue
            elif (
                sqrt(
                    (focus_pair[0] - points[j][0]) ** 2
                    + (focus_pair[1] - points[j][1]) ** 2
                )
                < min_dist
            ):
                min_dist = sqrt(
                    (focus_pair[0] - points[j][0]) ** 2
                    + (focus_pair[1] - points[j][1]) ** 2
                )
                close_pair = (focus_pair, points[j])
            else:
                continue
    return close_pair, min_dist


def main():
    # Generate random points
    num_points = 10_000
    print(f"Generating {num_points:,} random points...")
    points = generate_points(num_points, (0, 100), (0, 100))
    print("The first five random points are:")
    pprint(points[:5])
    print("Finding the closest pair of points:")

    # Measure time to find closest pair of points
    start_time = time.perf_counter()
    result = closest_pair(points)
    # result = slow_close_pair(points)
    elapsed_time = time.perf_counter() - start_time
    print("Nearest Points", end=": ")
    print(f"{result[0][0]} - {result[0][1]}")
    print(f"Minimum distance = {result[1]:.4f}")
    print(f"Time taken: {elapsed_time:.4f}")


if __name__ == "__main__":
    main()
