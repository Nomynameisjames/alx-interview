#!/usr/bin/python3
""" import files """
import sys
"""
    N queens problem is the challenge of placing N non-attacking queens on
    an N×N chessboard.
    Objectives:
    1- If user calle program with wrong number of args
            print Usage: nqueens N, followed by a new line, exit
            with the status 1
    2- while int(N) >= 4
            If N is not an int
                print N must be a number, followed by a new line,
                exit with the status 1
            elIf N is smaller than 4
                print N must be at least 4, followed by a new line,
                exit with the status 1
    3- print every possible solution to the problem followed by a new line
"""

""" objective 1 """
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

""" objective 2 """
try:
    N: int = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

""" objective 2 """
if N < 4:
    print("N must be at least 4")
    exit(1)

"""
    objective 3
    creates a list of length n with each element initialized to -1
"""
chessboard = [-1 for i in range(N)]


def safe_spot(row: int, col: int) -> bool:
    """
        checks if a spot is safe by checking if there is a queen in the same
        column or diagonal
    """
    for i in range(row):
        if chessboard[i] == col or abs(chessboard[i] - col) == abs(i - row):
            return False
    return True


def print_board() -> None:
    """
        prints the board in a nested lists format
    """
    global chessboard
    print([[i, chessboard[i]] for i in range(N)])


def nqueens(row: int) -> None:
    global chessboard
    """ base case """
    if row == N:
        print_board()
        return
    for col in range(N):
        """ check if spot is safe """
        if safe_spot(row, col):
            """ place queen """
            chessboard[row] = col
            """ move to next row """
            nqueens(row + 1)
            """ if no solution is found, backtrack """
        chessboard[row] = -1


if __name__ == "__main__":
    nqueens(0)
