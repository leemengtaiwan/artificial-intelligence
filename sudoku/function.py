from utils import *



def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    grid_dic = {}
    default_value = '123456789'
    for box, v in zip(boxes, grid):
        grid_dic[box] = v if v != '.' else default_value
    return grid_dic


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved_values = {box: v for box, v in values.items() if len(v) == 1}
    values_elim = dict(values)

    for box, digit in solved_values.items():
        for peer in peers[box]:
            values_elim[peer] = values_elim[peer].replace(digit, '')
    return values_elim


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    values_after = dict(values)
    for unit in unitlist:
        for digit in '123456789':
            digit_boxes = [box for box in unit if digit in values[box]]
            if len(digit_boxes) == 1:
                values_after[digit_boxes[0]] = digit
    return values_after


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    """Using depth-first search and propagation,
    create a search tree and solve the sudoku.
    """
    
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if not values: return values  # fail case

    # Choose one of the unfilled squares with the fewest possibilities
    box, digits = min(values.items(),
                      key=lambda x: len(x[1]) if len(x[1]) != 1 else 10)

    if len(digits) == 1:
        # print('Sudoku solved.(no square with > 1 digit)')
        return values
    else:
        for digit in digits:
            values_simulate = dict(values)
            values_simulate[box] = digit
            attempt = search(values_simulate)
            if attempt:
                return attempt


def grid_values_v1(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, grid))




