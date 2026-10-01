import numpy as np
import matplotlib.pyplot as plt

from math import pi
from random import random


def find_last_corner(c0: tuple, c1: tuple) -> list[tuple]:
    """This function calculates the last corner of the equilateral triangle. 

    Args:
        c0 (tuple): first corner of the triangle 
        c1 (tuple): second corner of the triangle

    Returns:
        list[tuple]: All the three corners of the triangle as a list of numpy arrays
    """
    dx = c1[0] - c0[0]
    dy = c1[1] - c0[1]

    alpha = 60./180*pi
    # rotate the displacement vector and add the result back to the original point
    xp = c0[0] + np.cos(alpha)*dx + np.sin(alpha)*dy
    yp = c0[1] + np.sin(alpha)*dx + np.cos(alpha)*dy

    # Creates the last coordinate as a tuple
    c2 = (xp, yp)

    # Corners are saved as a list of numpy arrays
    corners = [c0, c1, c2]
    return corners


def pick_start_point(corners: list[tuple]) -> tuple:
    """Creates a random start point inside the triangle

    Args:
        corners (list[tuple]): List with the coordinates of the vetices of the triangle

    Returns:
        tuple: Coordinates of the start point as a tuple
    """
    weight = []
    for corner in corners:
        weight.append(random())
    s = sum(weight)
    weight = [i * 1/s for i in weight]

    x = 0.0
    y = 0.0
    for i in range(len(corners)):
        x += weight[i]*corners[i][0]
        y += weight[i]*corners[i][1]
    X = (x, y)
    return X


def next_point(X: tuple, corners: list[tuple], N: int) -> tuple(list):
    """Find the next point by first picking a corner at random, 
    and then moving halfway between the current point and that corner.
    The first 5 points get ignore, while the remaining points get saved. 

    Args:
        X (tuple): current point insde the triangle
        corners (list[tuple]): list with the coordinates of the corners of the triangle as tuples
        N (int): amount of points that get saved as a list of numpy arrays

    Returns:
        tuple(list): List with the chosen amount of points, and list with the corner chosen in every point  
    """
    points = []
    indices = []
    for i in range(N+5):
        j = np.random.randint(0, 3)
        indices.append(j)
        new_x = (X[0] + corners[j][0])/2
        new_y = (X[1] + corners[j][1])/2
        X = (new_x, new_y)
        points.append(X)
    return points[5:], indices[5:]


def color(indices: list) -> list:
    """Decides the color of the point depending on which corner was used to create the point

    Args:
        indices (list): List of the corners used to create each point

    Returns:
        list: List of the assign color for each point
    """
    color = ['red', 'blue', 'green']
    colors = []
    for index in indices:
        colors.append(color[index])
    return colors


def RGB_color(indices: list) -> list[tuple]:
    """Assign an RBG color to each point depending on the corner used to create that point

    Args:
        indices (list): List of the corners used to create each point

    Returns:
        list[tuple]: List with the color for each point in RGB form
    """
    C = [(0, 0, 0)]
    for i in range(len(indices)-1):
        if indices[i] == 0:
            r = (1, 0, 0)
        elif indices[i] == 1:
            r = (0, 1, 0)
        elif indices[i] == 2:
            r = (0, 0, 1)
        c_0 = (C[i][0]+r[0])/2
        c_1 = (C[i][1]+r[1])/2
        c_2 = (C[i][2]+r[2])/2
        C.append((c_0, c_1, c_2))
    return C


if __name__ == '__main__':
    corners = find_last_corner((0, 0), (1, 0))
    start_point = pick_start_point(corners)
    points = next_point(start_point, corners, 10000)
    colors = RGB_color(points[1])
    points = points[0]
    plt.scatter(*zip(*points), c=colors, s=0.1, marker='.')
    plt.axis('equal')
    plt.axis('off')
    plt.show()
