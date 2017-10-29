"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import timeit

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)

        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)


    # def test_minimax(self):
    #
    #     player = self.player1
    #
    #
    #     print("active player: {}, Player location: {}, Is winner: {}, Utility:{}".format(
    #         self.game.active_player, self.game.get_player_location((self.game.active_player)),
    #         self.game.is_winner((self.game.active_player)), self.game.utility((self.game.active_player))
    #     ))
    #     print("Legal moves:", self.game.get_legal_moves())
    #
    #     print('Get move by minimax..')
    #

    #
    #     print('Best move: ', player.get_move(self.game, time_left))

    # def test_custom_score(self):
    #     start_move = (0, 0)
    #     self.game.apply_move(start_move)
    #     print("Assume player 1 move to", start_move , " score:",
    #           self.player1.score(self.game, self.player1))
    #     print(self.game.to_string())
    #
    #     # player 2 try
    #     for move in self.game.get_legal_moves():
    #         new_game = self.game.forecast_move(move)
    #         print('Player 2 move to {}, score for player1: {}'.format(
    #             move, self.player1.score(new_game, self.player1)
    #         ))
    #         print(new_game.to_string())

    def test_min_value(self):
        print()
        self.game.apply_move((0, 0))
        self.game.apply_move((1, 0))
        self.game.apply_move((2, 0))
        self.game.apply_move((2, 2))
        print(self.game.to_string())



        time_limit = 30
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda: time_limit - (time_millis() - move_start)

        print('Best move: ', self.player1.get_move(self.game, time_left))




if __name__ == '__main__':
    unittest.main()
