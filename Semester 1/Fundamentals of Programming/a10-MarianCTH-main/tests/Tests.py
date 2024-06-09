import unittest
from unittest.mock import patch
from board.Board import Board
from player.Player import Player
from game.Game import Game
from ui.Console import Console


class TestBattleshipGame(unittest.TestCase):
    def setUp(self):
        self.board_size = 10
        self.first_player_board = Board(self.board_size)
        self.second_player_board = Board(self.board_size)
        self.first_player = Player("Human")
        self.second_player = Player("Computer")
        self.game = Game(self.first_player_board, self.second_player_board, self.first_player, self.second_player)
        self.ui = Console(self.game)

    def test_place_ships(self):
        self.game.place_ships(1)
        self.assertTrue(any('S' in row for row in self.first_player_board.get_grid()))

    def test_make_player_move_invalid_format(self):
        with patch('builtins.input', return_value="A"):
            with self.assertRaisesRegex(Exception, "Invalid move. Please try again !2"):
                self.game.make_player_move("", "First")

    def test_make_player_move_hit(self):
        self.second_player_board.set_square(1, 1, "S")
        result = self.game.make_player_move("A1", "First")
        self.assertEqual(result, "HIT")

    def test_make_player_move_miss(self):
        self.second_player_board.set_square(1, 1, ' ')
        result = self.game.make_player_move("A1", "First")
        self.assertEqual(result, "MISS")

    def test_get_player_name_win_first_player(self):
        self.first_player_board.place_ships()
        self.assertEqual(self.game.get_player_name_win(), self.second_player.get_name())

    def test_get_player_name_win_second_player(self):
        self.second_player_board.place_ships()
        self.assertEqual(self.game.get_player_name_win(), self.first_player.get_name())

if __name__ == '__main__':
    unittest.main()
