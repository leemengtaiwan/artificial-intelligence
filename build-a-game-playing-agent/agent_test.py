"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import timeit

import isolation
import game_agent
from sample_players import center_score, open_move_score

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)

        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

        time_limit = 30
        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda: time_limit - (time_millis() - move_start)
        self.timeleft = time_left


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

    # def test_min_value(self):
    #     print()
    #     self.game.apply_move((0, 0))
    #     self.game.apply_move((1, 0))
    #     self.game.apply_move((2, 0))
    #     self.game.apply_move((2, 2))
    #     print(self.game.to_string())
    #
    #
    #
        # time_limit = 30
        # time_millis = lambda: 1000 * timeit.default_timer()
        # move_start = time_millis()
        # time_left = lambda: time_limit - (time_millis() - move_start)
    #
    #     print('Best move: ', self.player1.get_move(self.game, time_left))

    def test_alphabeta_center_dist_depth_1(self):
        """
        Make sure that you choose the first branch with the max score at the top level;
        branches searched later that return the same max score may only be returning an upper bound.
        """
        player1 = game_agent.AlphaBetaPlayer(search_depth=1, score_fn=center_score)
        player2 = "Player2"
        game = isolation.Board(player1, player2, width=9, height=9)
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                             0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 30]
        # print(game.to_string())
        best_move = player1.get_move(game, self.timeleft)
        # print(best_move)
        assert best_move == (1, 2), "Expected Best Move from AB Search: {}".format((1, 2))



if __name__ == '__main__':
    unittest.main()
