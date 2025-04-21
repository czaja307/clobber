def simple_heuristic(game):
    """
    A simple heuristic function that evaluates the board state.
    It counts the number of pieces for each player and returns the difference.
    """
    black_count = sum(row.count("B") for row in game.board)
    white_count = sum(row.count("W") for row in game.board)
    return black_count - white_count
