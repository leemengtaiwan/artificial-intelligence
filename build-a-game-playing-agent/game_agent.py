"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
from collections import deque
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """This evaluation try to give higher score to game state where opponent's
    moves are less AFTER player move.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    score = float(10 * player_moves - opponent_moves)
    if opponent_moves == 0:
        score *= 2
    return score


def custom_score_2(game, player):
    """This evaluation use the difference between number of available moves of
    the player and the number of available moves of the opponent as heuristic value.

    score = #available_moves(player) - #available_moves(opponent)

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(player_moves - opponent_moves)


def custom_score_3(game, player):
    """This evaluation use the number of available moves of the player in
    current game state as a heuristic value.

    score = #available_moves(player)

    Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return float(len(game.get_legal_moves(player)))


def custom_score_4(game, player):
    """This evaluation try to give higher score to game state where opponent's
    moves are less AFTER player move.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    open_moves = game.get_legal_moves(player)
    num_moves = len(open_moves)
    total_opponent_moves = 0
    opponent = game.get_opponent(player)
    for move in open_moves:
        new_game = game.forecast_move(move)
        total_opponent_moves += len(new_game.get_legal_moves(opponent))

    try:
        return -float(total_opponent_moves / float(num_moves))
    except ZeroDivisionError:
        return 0.


def custom_score_5(game, player):
    """This evaluation try to give higher score to game state where opponent's
    moves are less AFTER player move.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    score = float(player_moves - opponent_moves)
    if opponent_moves == 0:
        score *= 2
    return score


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout



class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)
        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def terminal_test(self, game):
        """ Return True if the game is over for the active player
        and False otherwise.
        """
        return False if game.get_legal_moves() else True

    def min_value(self, game, cur_depth):
        """Return the minimum of all maximum utilities generated by
        MinimaxPlayer in response to all possible legal moves made by the opponent
        in the given game state.

        Stop propagating child nodes and return utility of current game state
        when the conditions below meet:
        - No legal moves available for the game / game already ended
        - Reach depth limitation

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        cur_depth : int
            Indicate current depth level. If cur_depth reach depth limitation
            specified by self.search_depth (cur_depth >= self.search_depth),
            return current heuristic value of game without further search.

        Returns
        -------
        float
            The minimum utility over all legal child nodes
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if self.terminal_test(game) or cur_depth >= self.search_depth:
            return self.score(game, self)
        v = float("inf")
        for move in game.get_legal_moves():
            v = min(v, self.max_value(game.forecast_move(move), cur_depth + 1))
        return v

    def max_value(self, game, cur_depth):
        """Return the maximum of all minimum utilities generated by
        opponent in response to all possible legal moves made by the MinimaxPlayer
        in the given game state.

        Stop propagating child nodes and return utility of current game state
        when the conditions below meet:
        - No legal moves available for the game / game already ended
        - Reach depth limitation

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        cur_depth : int
            Indicate current depth level. If cur_depth reach depth limitation
            specified by self.search_depth (cur_depth >= self.search_depth),
            return current heuristic value of game without further search.

        Returns
        -------
        float
            The maximum utility over all legal child nodes
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if self.terminal_test(game) or cur_depth >= self.search_depth:
            return self.score(game, self)
        v = float("-inf")
        for move in game.get_legal_moves():
            v = max(v, self.min_value(game.forecast_move(move), cur_depth + 1))
        return v

    def minimax(self, game, depth):
        """Return a best move for the given game state using depth-limited
        minimax search algorithm described here:
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudo code) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves(self)
        if not legal_moves:
            return -1, -1
        _, move = max([(self.min_value(game.forecast_move(m), 1), m) for m in legal_moves])
        return move

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left, alpha=float("-inf"), beta=float("inf")):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        best_moves = deque([(-1, -1)])

        try:
            # iterative deepening search while time available
            def depths(n=100000):
                for e in range(n): yield e
            for depth in depths():
                best_moves.appendleft(self.alphabeta(game, depth, alpha, beta))

        except SearchTimeout:
            # return the best move from last completed search
            return best_moves[0]

        # Return the best move from the last completed search iteration
        return best_moves[0]

    def terminal_test(self, game):
        """ Return True if the game is over for the active player
        and False otherwise.
        """
        return False if game.get_legal_moves() else True

    def min_value(self, game, cur_depth, alpha, beta):
        """Return the minimum of all maximum utilities generated by
        MinimaxPlayer in response to all possible legal moves made by the opponent
        in the given game state.

        Stop propagating child nodes and return utility of current game state
        when the conditions below meet:
        - No legal moves available for the game / game already ended
        - Reach depth limitation

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        cur_depth : int
            Indicate current depth level. If cur_depth reach depth limitation
            specified by self.search_depth (cur_depth >= self.search_depth),
            return current heuristic value of game without further search.

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        float : The minimum utility over all legal child nodes
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if self.terminal_test(game) or cur_depth >= self.search_depth:
            return self.score(game, self)

        v = float("inf")
        for move in sorted(game.get_legal_moves()):
            v = min(v, self.max_value(game.forecast_move(move), cur_depth + 1, alpha, beta))
            if v <= alpha: return v
            beta = min(beta, v)
        return v

    def max_value(self, game, cur_depth, alpha, beta):
        """Return the maximum of all minimum utilities generated by
        opponent in response to all possible legal moves made by the MinimaxPlayer
        in the given game state.

        Stop propagating child nodes and return utility of current game state
        when the conditions below meet:
        - No legal moves available for the game / game already ended
        - Reach depth limitation

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        cur_depth : int
            Indicate current depth level. If cur_depth reach depth limitation
            specified by self.search_depth (cur_depth >= self.search_depth),
            return current heuristic value of game without further search.

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        float : The maximum utility over all legal child nodes
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if self.terminal_test(game) or cur_depth >= self.search_depth:
            return self.score(game, self)

        v = float("-inf")
        for move in sorted(game.get_legal_moves()):
            v = max(v, self.min_value(game.forecast_move(move), cur_depth + 1, alpha, beta))
            if v >= beta: return v
            alpha = max(alpha, v)
        return v

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves(self)
        if not legal_moves:
            return -1, -1

        best_move = -1, -1
        best_value = float("-inf")
        # sorted and ">" are needed to choose the left-most branch with max utility
        for move in sorted(legal_moves):
            v = self.min_value(game.forecast_move(move), 1, alpha, beta)
            if v > best_value:
                best_value = v
                best_move = move
            alpha = max(alpha, v)
        return best_move
