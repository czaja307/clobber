class Player:
    def __init__(self, game, color, heuristic, depth=3):
        self.game = game
        self.color = color
        self.heuristic = heuristic
        self.depth = depth

    def get_valid_moves(self):
        self.game.get_valid_moves(self.color)

    def make_move(self, start_row, start_col, end_row, end_col):
        self.game.make_move(start_row, start_col, end_row, end_col, self.color)

    def choose_move_minimax(self):
        """Use minimax to find the best move"""
        valid_moves = self.game.get_valid_moves(self.color)
        if not valid_moves:
            return None

        best_score = float('-inf')
        best_move = None

        for move in valid_moves:
            start_row, start_col, end_row, end_col = move

            # Make move directly on the game
            self.game.make_move(start_row, start_col, end_row, end_col, self.color)

            # Get score from minimax
            score = self._minimax(self.game, self.depth - 1, False)

            # Undo move
            self.game.undo_move(start_row, start_col, end_row, end_col, self.color)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _minimax(self, game, depth, is_maximizing):
        """Minimax algorithm implementation with move/undo"""
        if depth == 0:
            return self.heuristic(game) if self.color == "B" else -self.heuristic(game)

        current_player = self.color if is_maximizing else ("W" if self.color == "B" else "B")
        valid_moves = game.get_valid_moves(current_player)

        if not valid_moves:  # Game over
            return float('-inf') if is_maximizing else float('inf')

        best_score = float('-inf') if is_maximizing else float('inf')

        for move in valid_moves:
            start_row, start_col, end_row, end_col = move

            # Make move
            game.make_move(start_row, start_col, end_row, end_col, current_player)

            # Evaluate position
            score = self._minimax(game, depth - 1, not is_maximizing)

            # Undo move
            game.undo_move(start_row, start_col, end_row, end_col, current_player)

            # Update best score
            if is_maximizing:
                best_score = max(best_score, score)
            else:
                best_score = min(best_score, score)

        return best_score

    def choose_move_alpha_beta(self):
        """Use minimax with alpha-beta pruning to find the best move"""
        valid_moves = self.game.get_valid_moves(self.color)
        if not valid_moves:
            return None

        best_score = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')

        for move in valid_moves:
            start_row, start_col, end_row, end_col = move

            # Make move
            self.game.make_move(start_row, start_col, end_row, end_col, self.color)

            # Evaluate
            score = self._alpha_beta(self.game, self.depth - 1, alpha, beta, False)

            # Undo move
            self.game.undo_move(start_row, start_col, end_row, end_col, self.color)

            if score > best_score:
                best_score = score
                best_move = move

            alpha = max(alpha, best_score)

        return best_move

    def _alpha_beta(self, game, depth, alpha, beta, is_maximizing):
        """Alpha-beta pruning with move/undo"""
        if depth == 0:
            return self.heuristic(game) if self.color == "B" else -self.heuristic(game)

        current_player = self.color if is_maximizing else ("W" if self.color == "B" else "B")
        valid_moves = game.get_valid_moves(current_player)

        if not valid_moves:  # Game over
            return float('-inf') if is_maximizing else float('inf')

        if is_maximizing:
            max_score = float('-inf')
            for move in valid_moves:
                start_row, start_col, end_row, end_col = move

                # Make move
                game.make_move(start_row, start_col, end_row, end_col, current_player)

                # Evaluate
                score = self._alpha_beta(game, depth - 1, alpha, beta, False)

                # Undo move
                game.undo_move(start_row, start_col, end_row, end_col, current_player)

                max_score = max(max_score, score)
                alpha = max(alpha, max_score)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_score
        else:
            min_score = float('inf')
            for move in valid_moves:
                start_row, start_col, end_row, end_col = move

                # Make move
                game.make_move(start_row, start_col, end_row, end_col, current_player)

                # Evaluate
                score = self._alpha_beta(game, depth - 1, alpha, beta, True)

                # Undo move
                game.undo_move(start_row, start_col, end_row, end_col, current_player)

                min_score = min(min_score, score)
                beta = min(beta, min_score)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_score

    def __str__(self):
        return f"Player {self.color}"
