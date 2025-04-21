from heuristics import simple_heuristic
from game import Clobber, get_other_player
from player import Player
import time


def run_game_with_algorithm(algorithm_name):
    game = Clobber(7, 7)

    player_black = Player(game, "B", simple_heuristic, depth=3)
    player_white = Player(game, "W", simple_heuristic, depth=3)

    move_times = []
    moves_count = 0

    print(f"\nRunning game with {algorithm_name}:")

    while True:
        if algorithm_name == "minimax":
            if game.player_turn == "B":
                start_time = time.time()
                move = player_black.choose_move_minimax()
                end_time = time.time()
            else:
                start_time = time.time()
                move = player_white.choose_move_minimax()
                end_time = time.time()
        else:  # alpha-beta
            if game.player_turn == "B":
                start_time = time.time()
                move = player_black.choose_move_alpha_beta()
                end_time = time.time()
            else:
                start_time = time.time()
                move = player_white.choose_move_alpha_beta()
                end_time = time.time()

        move_time = end_time - start_time
        move_times.append(move_time)
        print(f"Move {moves_count + 1}: {move_time:.4f} seconds")

        if move is None:
            print(f"Game over! Player {get_other_player(game.player_turn)} won.")
            break

        start_row, start_col, end_row, end_col = move
        game.make_move(start_row, start_col, end_row, end_col, game.player_turn)
        moves_count += 1

    total_time = sum(move_times)
    avg_time = total_time / len(move_times) if move_times else 0

    return {
        "total_time": total_time,
        "avg_time": avg_time,
        "moves_count": moves_count
    }


if __name__ == "__main__":
    # Run game with standard minimax
    minimax_results = run_game_with_algorithm("minimax")

    # Run game with alpha-beta pruning
    alpha_beta_results = run_game_with_algorithm("alpha-beta")

    # Compare the results
    print("\n=== Performance Comparison ===")
    print(f"Standard Minimax:")
    print(f"  - Total time: {minimax_results['total_time']:.4f} seconds")
    print(f"  - Average time per move: {minimax_results['avg_time']:.4f} seconds")
    print(f"  - Moves completed: {minimax_results['moves_count']}")

    print(f"\nAlpha-Beta Pruning:")
    print(f"  - Total time: {alpha_beta_results['total_time']:.4f} seconds")
    print(f"  - Average time per move: {alpha_beta_results['avg_time']:.4f} seconds")
    print(f"  - Moves completed: {alpha_beta_results['moves_count']}")

    speedup = minimax_results['total_time'] / alpha_beta_results['total_time'] if alpha_beta_results[
                                                                                      'total_time'] > 0 else 0
    print(f"\nAlpha-Beta is {speedup:.2f}x faster than standard Minimax")
