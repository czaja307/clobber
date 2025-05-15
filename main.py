import time

from heuristics import simple_heuristic
from game import Clobber, get_other_player
from player import Player

if __name__ == "__main__":
    game = Clobber(10, 10)

    heuristic = simple_heuristic

    player_black = Player(game, "B", heuristic)
    player_white = Player(game, "W", heuristic)

    start_time = time.time()  # Start the timer

    while True:
        print(game)
        if game.player_turn == "B":
            move = player_black.choose_move_alpha_beta()
        else:
            move = player_white.choose_move_alpha_beta()

        if move is None:
            print(
                f"Game over! Player {get_other_player(game.player_turn)} won."
                f" Player {game.player_turn} has no valid moves.")
            break

        start_row, start_col, end_row, end_col = move
        game.make_move(start_row, start_col, end_row, end_col, game.player_turn)

    end_time = time.time()  # End the timer
    print(f"Total program execution time: {end_time - start_time:.4f} seconds")
