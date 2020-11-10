from constraints import CSP

def constraint_check(CSP, answer, cell, value):
    """
    From a given cell, goes through and checks all of a cells neighbours,
    if there are no constraint conflicts, return no_cons.
    """
    no_cons = True

    for c_cell, c_val in answer.items():
        if c_cell in CSP.neighbour_cells[cell] and c_val == value:
            no_cons = False

    return no_cons


def assign(CSP, cell, value, answer):
    """
    Given a cell that is going to be placed into 
    the answer list.
    Checks forward checks for any constraint conflicts 
    """
    answer[cell] = value

    if CSP.possibilities:
        forward_check(CSP, cell, value, answer)
    return


def unassign(CSP, cell, answer):
    """
    Takes an old choice from backtrack
    places the old choice back into the possibilites of each cell
    and gets rid of choice from pruned
    """

    if cell in answer:
        for (spot,value) in CSP.pruned[cell]:
            CSP.possibilities[spot].append(value)
        CSP.pruned[cell] = []
        answer.pop(cell)

    return

def forward_check(CSP, cell, value, answer):
    """
    Reduces the amount of possibilites left for values to be chosen from
    due to cells in front of it.
    """
    for neighbour in CSP.neighbour_cells[cell]:
        if neighbour not in answer:
            if value in CSP.possibilities[neighbour]:
                CSP.possibilities[neighbour].remove(value)
                CSP.pruned[cell].append((neighbour, value))
    return

def is_diff(cell_a, cell_b):
    """
    Checks if two values share the same value, if not, return false.
    """
    if cell_a != cell_b:
        return True
    return False