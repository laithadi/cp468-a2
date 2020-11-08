from readingInput import readInputTxtFile
from temp import createCell  
from cell import Cell
from constraints import constraints

SUDOKU = readInputTxtFile() 
CELLS = createCell(SUDOKU)

cell_queue = []
for cell in CELLS.keys():
    cell_queue.append(CELLS[cell])

cell_queue_copy = []
for cell in CELLS.keys():
    cell_queue.append(CELLS[cell])

def AC3(csp):
    
    """ 
    Uses the CSP or arc consistency to check each individual constraint.
    Returns False if an inconsistency is found within the constraints, 
    otherwise True
    
    """
    

    # return
    while cell_queue:
        Xi = cell_queue.pop(0)

        if revise(cell_queue_copy, Xi):
    
            if len(Xi.domain) == 0:
                return False

            for X in Xi.domain:
                if X != Xi.domain[X]:
                    cell_queue.append(Xi.domain[X])
            """ 
            This is here so that it will append the next value in domain,
            such that X != a value in the domain.
            Not sure if this is proper yet.
            """


    return True

    # If you can think of any possible ideas for what else we would need to check 
    # inside of the AC3 algo, just leave it here

    # MAKE SURE TO UPDATE THE CELL_QUEUE WITH THE RIGHT DOMAINS AFTER REVISE()


def revise(cell_queue, Xi):
    """
    Takes the current cell popped from the sudoku board, 
    makes a list of values from the domain of the cell.
    Checks each individual value in the domain with the constraints,
    if the constraints are false, it will remove this value from the domain.
    What is left is the viable options that can be chose at the specific cell
    for the algorithm to try with.
    """

    revised = False

    for dom in Xi.domain:
        if not constraints(cell_queue_copy, Xi, dom):
            cell_queue.domain[Xi].remove(dom)
            revised = True
    return revised


