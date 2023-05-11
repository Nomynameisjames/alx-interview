#!/usr/bin/python3
""" import files """
import sys

"""
    N-Queens Problem
    The N-Queens problem is the problem of placing N chess queens on an N x N
    chessboard so that no two queens threaten each other. a solution requires
    that no two queens share the same row, column, or diagonal.
"""


class NQueensSolver:
    """
        class that solves the NQueens problem
    """
    def __init__(self, n: int):
        self.n = n
        self.chessboard = [-1 for i in range(n)]

    def solve(self):
        self.nqueens(0)

    def safe_spot(self, row: int, col: int) -> bool:
        """
            Checks if a spot is safe by checking if there is a queen in the
            same column or diagonal
        """
        for i in range(row):
            if self.chessboard[i] == col or abs(self.chessboard[i] - col)\
                    == abs(i - row):
                return False
        return True

    def print_board(self) -> None:
        """
            Prints the board in a nested lists format
        """
        print([[i, self.chessboard[i]] for i in range(self.n)])

    def nqueens(self, row: int) -> None:
        """
            Solves the NQueens problem recursively using backtracking
        """
        if row == self.n:
            self.print_board()
            return

        for col in range(self.n):
            if self.safe_spot(row, col):
                self.chessboard[row] = col
                self.nqueens(row + 1)
                self.chessboard[row] = -1


def main(args: list):
    """
        Main function
    """
    if len(args) != 2:
        print("Usage: nqueens N")
        return 1

    try:
        n = int(args[1])
    except ValueError:
        print("N must be a number")
        return 1

    if n < 4:
        print("N must be at least 4")
        return 1

    solver = NQueensSolver(n)
    solver.solve()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
