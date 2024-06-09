from board.Board import Board
from player.Player import Player
from game.Game import Game
from ui.Console import Console
from ui.gui import GUI


def play_game():
    board_size = 10
    first_player_board = Board(board_size)
    second_player_board = Board(board_size)

    first_player = Player("Human")
    second_player = Player("Computer")

    game = Game(first_player_board, second_player_board, first_player, second_player)
    ui = Console(game)
    #ui = GUI(game)
    ui.start()

if __name__ == "__main__":
    play_game()
