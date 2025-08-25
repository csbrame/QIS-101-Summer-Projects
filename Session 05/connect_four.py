#!/usr/bin/env python3
"""connect_four.py"""


def check_winner(player, board):
    """Function to check if a given player has won the game. Takes in the player
    number, the board configuration. Returns True if the player has a win, False
    if the player has no win."""
    # Initialize an empty list called tiles
    tiles = []
    # Iterate through the board, if a spot is occupied by the player, add its coordinates to the list
    for i in range(5, -1, -1):
        for j in range(len(board[i])):
            if board[i][j] == player:
                tiles.append((j, i))
    # Iterate through the list, see if there are three adjacent pieces for each tile
    for j in range(len(tiles)):
        focus_tile = tiles[j]
        if (
            (
                (focus_tile[0] + 1, focus_tile[1]) in tiles
                and (focus_tile[0] + 2, focus_tile[1]) in tiles
                and (focus_tile[0] + 3, focus_tile[1]) in tiles
            )
            or (
                (focus_tile[0], focus_tile[1] + 1) in tiles
                and (focus_tile[0], focus_tile[1] + 2) in tiles
                and (focus_tile[0], focus_tile[1] + 3) in tiles
            )
            or (
                (focus_tile[0] + 1, focus_tile[1] + 1) in tiles
                and (focus_tile[0] + 2, focus_tile[1] + 2) in tiles
                and (focus_tile[0] + 3, focus_tile[1] + 3) in tiles
            )
            or (
                (focus_tile[0] + -1, focus_tile[1] + 1) in tiles
                and (focus_tile[0] - 2, focus_tile[1] + 2) in tiles
                and (focus_tile[0] - 3, focus_tile[1] + 3) in tiles
            )
        ):
            return True
        else:
            continue
    return False


def print_winner(board):
    """Print the winner, if there is one. Takes board as input and prints out the winner."""
    print(*board, sep="\n")
    # Check if a winner is on the board. If not, call out no winner yet
    if check_winner(1, board):
        print("Player 1 wins!")
    else:
        if check_winner(2, board):
            print("Player 2 wins!")
        else:
            print("No winner yet")
    print()


def main():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()
