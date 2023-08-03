#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys


def generate_solutions(row, column):
    """
    solve a simple N x N matrix
    Args:
        row (int): Number of rows
        column (int): Number of columns
    Returns:
        returns a list of lists
    """
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Place the queen at a certain position
    Args:
        queen (int): The queen
        column (int): The column to move
        prev_solution (list): the previous move
    Returns:
        returns a list
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    check if it's safe to make a move
    Args:
        q (int): row to move to
        x (int): column to move to
        array (array): the matrix
    Returns:
        returns a boolean
    """
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """
    Lets initialize the game shall we?
    Args:
        this function doesn't take any args
    Returns:
        returns an integer
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():
    """
    The main entry point
    Args:
        can be called without passing args
    Returns:
        returns None
    Example
    -----------------------
    """
    n = init()
    solutions = generate_solutions(n, n)
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()