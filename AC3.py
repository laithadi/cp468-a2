from readingInput import readInputTxtFile
from temp import createCell  
from cell import Cell
from constraints import CSP

SUDOKU = readInputTxtFile() 
CELLS = createCell(SUDOKU)




def revise(CSP, Xa, Xb):
    """
    Takes the current cell popped from the sudoku board, 
    makes a list of values from the domain of the cell.
    Checks each individual value in the domain with the constraints,
    if the constraints are false, it will remove this value from the domain.
    What is left is the viable options that can be chose at the specific cell
    for the algorithm to try with.
    """

    revised = False

    for val in CSP.possibilities[Xa]:
        if not constraints("isdifferent or new name"(value,x) for x in "csp.posibilites"[Xb]:
            CSP.possibilities[Xa].remove(value)
            revised = True
    return revised

    
def AC3(CSP, Queue):
    
    """ 
    Uses the CSP or arc consistency to check each individual constraint.
    Returns False if an inconsistency is found within the constraints, 
    otherwise True
    
    """
    if cspqueue == none:
        cspqueue = list(CSP.b_constraints)
    
    while cspqueue != None:
        (Xa,Xb) = cspqueue.pop()
        if revise(CSP, Xa, Xb):
            if len(CSP.possibilities[Xa])== 0:
                return False

        for cell in CSP.neighbour_cells[Xa]:
            if cell != Xa:
                cspqueue.append(cell, Xa)

    return True

    # If you can think of any possible ideas for what else we would need to check 
    # inside of the AC3 algo, just leave it here

    # MAKE SURE TO UPDATE THE CELL_QUEUE WITH THE RIGHT DOMAINS AFTER REVISE()





