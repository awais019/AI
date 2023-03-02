"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count number of X's and O's
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    # If X's and O's are equal, X plays next
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create empty set
    actions = set()
    # Add all empty cells to set
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Check if action is valid
    if action not in actions(board):
        raise Exception("Invalid action")

    # Create copy of board
    new_board = [[board[i][j] for j in range(3)] for i in range(3)]

    # Make move
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # If board is terminal, return None
    if terminal(board):
        return None

    # If it's X's turn, maximize
    if player(board) == X:
        return max_value(board)[1]

    # If it's O's turn, minimize
    else:
        return min_value(board)[1]


def max_value(board):
    """
    Returns the maximum value of the board
    """
    # If board is terminal, return utility
    if terminal(board):
        return utility(board), None

    # Initialize v to negative infinity
    v = -math.inf

    # Initialize best move to None
    best_move = None
    # For each action in actions(board)
    for action in actions(board):

        # Get the minimum value of the resulting board
        min_value_result = min_value(result(board, action))

        # If the minimum value is greater than v
        if min_value_result[0] > v:

            # Set v to the minimum value
            v = min_value_result[0]

            # Set best move to the current action
            best_move = action

    return v, best_move


def min_value(board):
    """
    Returns the minimum value of the board
    """
    # If board is terminal, return utility
    if terminal(board):
        return utility(board), None

    # Initialize v to positive infinity
    v = math.inf

    # Initialize best move to None
    best_move = None

    # For each action in actions(board)
    for action in actions(board):

        # Get the maximum value of the resulting board
        max_value_result = max_value(result(board, action))

        # If the maximum value is less than v
        if max_value_result[0] < v:

            # Set v to the maximum value
            v = max_value_result[0]

            # Set best move to the current action
            best_move = action

    return v, best_move
