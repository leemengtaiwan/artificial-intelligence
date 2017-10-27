

def terminal_test(game_state):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    return False if game_state.get_legal_moves() else True


def min_value(game_state):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(game_state):
        return 1
    else:
        return min([max_value(game_state.forecast_move(m)) \
                    for m in game_state.get_legal_moves()])


def max_value(game_state):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(game_state):
        return -1
    else:
        return max([min_value(game_state.forecast_move(m)) \
                    for m in game_state.get_legal_moves()])


# def min_value(game_state):
#     """ Return the value for a win (+1) if the game is over,
#     otherwise return the minimum value over all legal child
#     nodes.
#     """
#     if terminal_test(game_state):
#         return 1  # by Assumption 2
#     v = float("inf")
#     for m in game_state.get_legal_moves():
#         v = min(v, max_value(game_state.forecast_move(m)))
#     return v
#
#
# def max_value(game_state):
#     """ Return the value for a loss (-1) if the game is over,
#     otherwise return the maximum value over all legal child
#     nodes.
#     """
#     if terminal_test(game_state):
#         return -1  # by assumption 2
#     v = float("-inf")
#     for m in game_state.get_legal_moves():
#         v = max(v, min_value(game_state.forecast_move(m)))
#     return v