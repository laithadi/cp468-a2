from readingInput import readInputTxtFile
from temp import createCell  
from cell import Cell
from constraints import CSP
from helper import is_diff

SUDOKU = readInputTxtFile() 
CELLS = createCell(SUDOKU)





    
def AC3(CSP, Queue = None):
    
    """ 
    Uses the CSP or arc consistency to check each individual constraint.
    Returns False if an inconsistency is found within the constraints, 
    otherwise True
    
    """
    if cspqueue == None:
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
        if Xa != Xb:
            if not any ([is_diff(val,x) for x in CSP.possibilities[Xb]]):
                CSP.possibilities[Xa].remove(val)
                revised = True
    return revised






