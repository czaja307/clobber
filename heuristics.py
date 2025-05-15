import random

def piece_count_difference_heuristic(game):
    """
    A heuristic function that evaluates the board state by counting the number of pieces
    for each player and returning the difference (Black - White).
    """
    black_count = sum(row.count("B") for row in game.board)
    white_count = sum(row.count("W") for row in game.board)
    return black_count - white_count


def mobility_heuristic(game):
    """
    A heuristic function that evaluates the board state by counting the number of valid moves
    for each player. More available moves generally means more flexibility and control.
    
    Returns the difference in number of valid moves (Black - White).
    """
    black_moves = len(game.get_valid_moves("B"))
    white_moves = len(game.get_valid_moves("W"))
    return black_moves - white_moves


def center_control_heuristic(game):
    """
    A heuristic that gives more value to pieces controlling the center of the board,
    which typically provides more opportunities for moves.
    
    Returns a value favoring the player with better board position.
    """
    center_row = game.rows // 2
    center_col = game.cols // 2
    
    black_control = 0
    white_control = 0
    
    for row in range(game.rows):
        for col in range(game.cols):
            # Calculate distance from center (Manhattan distance)
            distance_from_center = abs(row - center_row) + abs(col - center_col)
            # Pieces closer to center get higher weight
            position_value = game.rows + game.cols - distance_from_center
            
            if game.board[row][col] == "B":
                black_control += position_value
            elif game.board[row][col] == "W":
                white_control += position_value
    
    return black_control - white_control


def grouping_heuristic(game):
    """
    A simple grouping heuristic that rewards players for having their pieces adjacent (orthogonally).
    For each piece, count the number of same-color neighbors. Returns (Black - White).
    """
    black_groups = 0
    white_groups = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for row in range(game.rows):
        for col in range(game.cols):
            piece = game.board[row][col]
            if piece in ("B", "W"):
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < game.rows and 0 <= nc < game.cols:
                        if game.board[nr][nc] == piece:
                            if piece == "B":
                                black_groups += 1
                            else:
                                white_groups += 1
    return black_groups - white_groups


def random_heuristic(game):
    """
    A very simple heuristic that returns a random value. Useful for testing or as a baseline.
    """
    return random.randint(-100, 100)



