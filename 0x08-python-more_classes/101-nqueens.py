#!/usr/bin/python3
"""
"""


if __name__ is "__main__":
    import sys
def main()
    """ """
    args = sys.argv
    if len(args) is not 2:
        print('Usage: nqueens N')
        sys.exit(1)

    n = args[1]
    # n must be integer >= 4
    if type(n) is not int:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exti(1)

    # create board
    board = [[0 for col in range(n)] for row in range(n)]

    for row in range(n):  # each possible placement
        for col in range(n):
            placed = 0
            while placed < n:
            
                if check_placement(board, [row, col]) is True:
                    # place queen
                    placed += 1

            print_board # print board
    return 0

def check_placement(board, pos)
    """Determine if the queen can safely assume position"""

    # check column

    # check diagnols

def print_board()
    """Prints board with queens safely positioned"""
