from minimax_helpers import *


def minimax_decision(game_state):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """
    return max([(m, min_value(game_state.forecast_move(m)))\
               for m in game_state.get_legal_moves()],
               key=lambda x: x[1])[0]
