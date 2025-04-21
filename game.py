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

    def is_valid_move(self, start_row, start_col, end_row, end_col, player):
        if player not in ["B", "W"]:
            return False, "Invalid move. The player must be 'B' or 'W'."
        if player != self.player_turn:
            return False, "Invalid move. It's not your turn."
        if (abs(start_row - end_row) + abs(start_col - end_col)) != 1:
            return False, "Invalid move. The move must be to an adjacent square."
        if start_row < 0 or start_row >= self.rows or end_row < 0 or end_row >= self.rows:
            return False, "Invalid move. The move must be within the board (row out of bounds)."
        if start_col < 0 or start_col >= self.cols or end_col < 0 or end_col >= self.cols:
            return False, "Invalid move. The move must be within the board (column out of bounds)."
        if self.board[start_row][start_col] != player:
            return False, "Invalid move. The player must move their own piece."
        if self.board[end_row][end_col] != get_other_player(player):
            return False, "Invalid move. The destination must be an opponent's piece."
        return True, "Valid move."

    def get_valid_moves(self, player):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x in range(self.rows):
            for y in range(self.cols):
                if self.board[x][y] == player:
                    for dx, dy in directions:
                        is_valid, message = self.is_valid_move(x, y, x + dx, y + dy, player)
                        if is_valid:
                            moves.append((x, y, x + dx, y + dy))
        return moves

    def make_move(self, start_row, start_col, end_row, end_col, player):
        is_valid, message = self.is_valid_move(start_row, start_col, end_row, end_col, player)
        if not is_valid:
            raise ValueError(message)

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
    rows = 2
    cols = 3
    game = Clobber(rows, cols)
    print(game)

    print(game.get_valid_moves("B"))
