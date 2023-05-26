#!/usr/bin/python3
""" Island Perimeter """

"""
    objective: Create a function def island_perimeter(grid): that returns the
               perimeter of the island described in grid:
    1. grid is a list of list of integers:
        * 0 represents a water zone
        * 1 represents a land zone
        * One cell is a square with side length 1
        * Grid cells are connected horizontally/vertically (not diagonally).
        * Grid is rectangular, width and height don’t exceed 100
    2. Grid is completely surrounded by water
    3. There is only one island (or nothing).
    4. The island doesn’t have “lakes” (water inside that isn’t connected to
        the water surrounding the island).
"""


def island_perimeter(grid: list) -> int:
    """ Function that returns the perimeter of the island described in grid """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    return perimeter
