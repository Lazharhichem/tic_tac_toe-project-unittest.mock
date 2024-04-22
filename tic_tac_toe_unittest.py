import unittest
from unittest.mock import patch
from tic_tac_toe import TicTacToe, HumanPlayer

class TestTicTacToe(unittest.TestCase):
    def test_winner_horizontal(self):
        game = TicTacToe()
        game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(game.winner(0, 'X'))

    def test_winner_vertical(self):
        game = TicTacToe()
        game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
        self.assertTrue(game.winner(6, 'O'))

    def test_winner_diagonal(self):
        game = TicTacToe()
        game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(game.winner(0, 'X'))

    def test_draw(self):
        game = TicTacToe()
        game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertFalse(game.winner(0, 'X'))

    def test_human_player_get_move(self):
        player = HumanPlayer('X')
        with patch('builtins.input', return_value='1'):
            self.assertEqual(player.get_move(TicTacToe()), 1)

if __name__ == '__main__':
    unittest.main()
