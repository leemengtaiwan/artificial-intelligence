import copy


class GameState:
    """
    Attributes
    ----------
    _dim: tuple
        Represent the dimension of the board with (width, height)
        = (xlim, ylim), e.g., (3, 2) means the board look like
        [0 0 0]
        [0 0 0]

    _xlim: int
        width of the board

    _ylim: int
        height of the board

    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1

    _active_player: bool
        Keep track of active player initiative (which
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player 2

    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player 1 is at (0, 0) and player 2 is at (1, 0)

    """

    def __init__(self, xlim=3, ylim=2):
        self._xlim, self._ylim = xlim, ylim
        self._dim = (self._xlim, self._ylim)
        self._board = [[0] * self._ylim for _ in range(self._xlim)]
        self._active_player = 0
        self._player_locations = [None, None]
        self._board[-1][-1] = 1  # block lower-right corner

    def __str__(self):
        """Retrun a string representing current board
        as human-readable format
        """
        rows = [' '.join([str(col[y]) for col in self._board]) for y in range(self._ylim)]
        board_str = '\n'.join(rows)
        return board_str

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move.
            Note the position is zero-indexed.
        """
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")

        x, y = move
        new_state = copy.deepcopy(self)
        new_state._board[x][y] = 1
        new_state._player_locations[self._active_player] = move
        new_state._active_player ^= 1  # toggle active player
        return new_state


    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """

        # all squares are available when making first move
        if self._player_locations[1] == None:
            return [(x, y) for x, col in enumerate(self._board) \
                    for y, v in enumerate(col) if v != 1]

        # find valid squares from eight possible directions
        rays = [(-1, 0), (1, 0), (0, 1), (0, -1),
                (-1, 1), (1, -1), (-1, -1), (1, 1)]
        moves = []
        for dx, dy in rays:
            x, y = self._player_locations[self._active_player]

            while 0 <= x + dx < self._xlim and 0 <= y + dy < self._ylim:
                x, y = x + dx, y + dy
                if self._board[x][y]: break
                moves.append((x, y))

        return moves



