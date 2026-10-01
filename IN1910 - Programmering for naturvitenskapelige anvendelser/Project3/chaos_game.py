import re

import numpy as np
import matplotlib.pyplot as plt

from typing import Optional
from random import random


class ChaosGame:
    def __init__(self, n: int, r: Optional[float] = 1/2) -> None:
        if type(n) != int:
            raise ValueError('The amount of points needs to be a integer')
        elif n < 3:
            raise ValueError('The minimum amount of points needs to be 3')
        elif type(r) != float:
            raise ValueError('The r parameter needs to be a float')
        elif r > 1 or r < 0:
            raise ValueError('The r parameter needs to be between 0 and 1.')
        self.n = n
        self.r = r
        self.c = self._generate_ngon()

    def _generate_ngon(self) -> list[tuple]:
        """Generates all corners of the polygon so they are equaly apart 
        from the next/previous and have the same angle

        Returns:
            list[tuple]: list of the coordinates of the corners as tuple
        """
        delta_angle = 360 / self.n
        c = []
        for i in range(self.n):
            angle = (180 + i * delta_angle) * np.pi / 180
            c.append((np.sin(angle), np.cos(angle)))
        return c

    def plot_ngon(self) -> None:
        """Plots the corners of the polygon"""
        corners = self._generate_ngon()
        plt.scatter(*zip(*corners))
        plt.axis('off')
        plt.axis('equal')

    def _starting_point(self) -> tuple:
        """Creates a random start point inside the polygon

        Args:
            corners (list[tuple]): List with the coordinates of the vetices of the triangle

        Returns:
            tuple: Coordinates of the start point as a tuple
        """
        weight = []
        for corner in self.c:
            weight.append(random())
        s = sum(weight)
        weight = [i * 1/s for i in weight]

        x = 0.0
        y = 0.0
        for i in range(len(self.c)):
            x += weight[i]*self.c[i][0]
            y += weight[i]*self.c[i][1]
        X = (x, y)
        return X

    def iterate(self, steps: int, discard: Optional[int] = 5) -> None:
        """Creates a desired amount of points that are inside the polygon so that they can be plotted

        Args:
            steps (int): Amount of points
            discard (Optional[int], optional): Amount of points that get discarted at the beginning Defaults to 5.
        """
        X0 = self._starting_point()
        for i in range(discard):
            j = np.random.randint(0, self.n)
            new_x = self.r * X0[0] + (1-self.r) * self.c[j][0]
            new_y = self.r * X0[1] + (1-self.r) * self.c[j][1]
            X0 = (new_x, new_y)

        points = []
        points.append(X0)
        indices = []
        indices.append(j)
        for i in range(steps-1):
            j = np.random.randint(0, self.n)
            indices.append(j)
            new_x = self.r * X0[0] + (1-self.r) * self.c[j][0]
            new_y = self.r * X0[1] + (1-self.r) * self.c[j][1]
            X0 = (new_x, new_y)
            points.append(X0)
        self.points = points
        self.indices = indices

    def plot(self, color: Optional[bool] = False, cmap: Optional[str] = 'rainbow') -> None:
        """Plots the points created in iterated

        Args:
            color (bool, optional): decides if the points have color or they are black. Defaults to False.
            cmap (str, optional): a colormap gradient. Defaults to 'rainbo, so it goes from purple to red.
        """
        if color is False:
            colors = 'black'
        elif color is True:
            colors = self.gradient_color
        # elif color is False:
          #  color = 'black'
        plt.scatter(*zip(*self.points), c=colors, s=0.7, cmap=cmap)
        plt.axis('equal')
        plt.axis('off')

    def show(self, color: Optional[bool] = False, cmap: Optional[str] = 'rainbow') -> None:
        """Shows the plot

        Args:
            color (bool, optional): decides if the points have color or they are black. Defaults to False.
            cmap (str, optional): a colormap gradient. Defaults to 'rainbo, so it goes from purple to red.
        """
        self.plot(color, cmap)
        plt.show()

    @property
    def gradient_color(self) -> list[int]:
        """Creates a gradient color list so the points plotted will have gradient color

        Returns:
            list[int]: a list of gradient color values corresponding to the values in X
        """
        C = [self.indices[0]]
        for i in range(len(self.indices)-1):
            C.append((C[i]+self.indices[i+1])/2)
        return C

    def savepng(self, outfile: str, color: Optional[bool] = False, cmap: Optional[str] = 'rainbow') -> None:
        """Saves the plot as a png file with the desired name

        Args:
            outfile (str): name of the file to be saved
            color (bool, optional): decides if the points have color or they are black. Defaults to False.
            cmap (str, optional): a colormap gradient. Defaults to 'rainbo, so it goes from purple to red.

        Raises:
            TypeError: If the outfile has a different fileending than png, it raises an error
        """
        if not outfile.endswith('.png'):
            match = re.findall(r'\.[a-zA-Z]{3,4}$', outfile)
            if match != []:
                raise TypeError('The outfile type must be .png')
            outfile = outfile + '.png'
        self.plot(color, cmap)
        plt.savefig('figures/' + outfile, dpi=300, transparent=True)


if __name__ == "__main__":
    game = ChaosGame(4, 0.4)
    game.iterate(10000)
    game.show(color=True)
