"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

x-o-referee

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.
"""
from typing import List


def checkio(game_result: List[str]) -> str:
    for i in range(len(game_result)):
        for j in range(len(game_result[i])):
            if j == 0 and game_result[i][j] == "X" and game_result[i][j + 1] == "X" and game_result[i][j + 2] == "X":
                return "X"
            elif i == 0 and game_result[i][j] == "X" and game_result[i + 1][j] == "X" and game_result[i + 2][j] == "X":
                return "X"
            elif i == 0 and j == 0 and game_result[i][j] == "X" and game_result[i + 1][j + 1] == "X" and game_result[i + 2][j + 2] == "X":
                return "X"
            elif i == 0 and j == 0 and game_result[i][j + 2] == "X" and game_result[i + 1][j + 1] == "X" and game_result[i + 2][j] == "X":
                return "X"
    for i in range(len(game_result)):
        for j in range(len(game_result[i])):
            if j == 0 and game_result[i][j] == "O" and game_result[i][j + 1] == "O" and game_result[i][j + 2] == "O":
                return "O"
            elif i == 0 and game_result[i][j] == "O" and game_result[i + 1][j] == "O" and game_result[i + 2][j] == "O":
                return "O"
            elif i == 0 and j == 0 and game_result[i][j] == "O" and game_result[i + 1][j + 1] == "O" and game_result[i + 2][j + 2] == "O":
                return "O"
            elif i == 0 and j == 0 and game_result[i][j + 2] == "O" and game_result[i + 1][j + 1] == "O" and game_result[i + 2][j] == "O":
                return "O"
    return "D"


if __name__ == "__main__":
    print("Example:")
    print(checkio(["X.O", "XX.", "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
