class Clobber:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.player_turn = "B"

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = create_board(rows, cols)
        self.player_turn = "B"

    def is_valid_move(self, start_row, start_col, end_row, end_col, player, player_turn):
        if player not in ["B", "W"]:
            print("Error: The player must be 'B' or 'W'.")
            return False
        if player != player_turn:
            print("Error: It's not your turn.")
            return False
        if self.board[start_row][start_col] != player:
            print("Error: The player must move their own piece.")
            return False
        if self.board[end_row][end_col] != get_other_player(player):
            print("Error: The destination must be an opponent's piece.")
            return False
        if (abs(start_row - end_row) + abs(start_col - end_col)) != 1:
            print("Error: The move must be to an adjacent square.")
            return False
        if start_row < 0 or start_row >= self.rows or end_row < 0 or end_row >= self.rows:
            print("Error: The move must be within the board (row out of bounds).")
            return False
        if start_col < 0 or start_col >= self.cols or end_col < 0 or end_col >= self.cols:
            print("Error: The move must be within the board (column out of bounds).")
            return False
        return True

    def make_move(self, start_row, start_col, end_row, end_col, player):
        if not self.is_valid_move(start_row, start_col, end_row, end_col, player, self.player_turn):
            raise ValueError("Invalid move.")

        self.board[end_row][end_col] = player
        self.board[start_row][start_col] = "_"
        self.player_turn = get_other_player(self.player_turn)

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join(row) + "\n"
        return board_str


def create_board(rows, cols):
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i + j) % 2 == 0:
                row.append("B")
            else:
                row.append("W")
        board.append(row)
    return board


def get_other_player(player):
    if player == "B":
        return "W"
    if player == "W":
        return "B"
    else:
        raise ValueError("Invalid player. Player must be 'B' or 'W'.")


if __name__ == "__main__":
    rows = 5
    cols = 6
    game = Clobber(rows, cols)
    print(game)
    game.make_move(0, 0, 1, 0, "B")
    print(game)
    game.make_move(3, 0, 3, 1, "W")
    print(game)
