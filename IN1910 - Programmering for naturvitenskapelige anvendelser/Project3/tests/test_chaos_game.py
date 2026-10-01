import pytest
import math
import matplotlib.pyplot as plt
from chaos_game import ChaosGame
from pathlib import Path


@pytest.mark.parametrize(
    "n, r",
    [
        (3, 1),
        (3, -5),
        (1, 1/2),
    ],
)
def test_constructorn(n, r):
    try:
        ChaosGame(n, r)
    except ValueError:
        # Correct exception is raised, test should pass
        pass
    else:
        # No exception has been raised, test should fail
        raise Exception


@pytest.mark.parametrize(
    "n",
    [
        (3),
        (4),
        (5),
        (6),
        (7),
        (8),
    ],
)
def test_generate_ngon(n):
    game = ChaosGame(n)
    corners = game._generate_ngon()
    assert len(corners) == n
    sides = []
    for i in range(n):
        if i+1 < n:
            sides.append(pytest.approx(math.dist(corners[i], corners[i+1])))
    sides.append(pytest.approx(math.dist(corners[-1], corners[0])))
    assert len(sides) == n
    assert all(ele == sides[0] for ele in sides)
    # Remove comment mark to see the plots of the ngons
    # game.plot_ngon()
    # plt.show()


def test_iterate():
    game = ChaosGame(5)
    game.iterate(10000)
    points = game.points
    assert len(points) == 10000


@pytest.mark.parametrize(
    "n, r",
    [
        (3, 1/2),
        (4, 1/3),
        (5, 1/3),
        (5, 3/8),
        (6, 1/3),
    ],
)
def test_savepng(n, r):
    game = ChaosGame(n, r)
    game.iterate(10000)
    outfile = f'chaos_{n}_{r:.3f}'
    game.savepng(outfile, color=True)
    dest_dir = Path('figures')
    assert dest_dir.exists()
    assert list(dest_dir.glob(outfile + '.png'))
    # How can I make that the plot is empty before using the next parameter
    # While ploting one parameter at a time it plots the images shown in the Readme file
