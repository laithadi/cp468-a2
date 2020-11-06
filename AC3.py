from readingInput import readInputTxtFile
from temp import createCell  
from cell import Cell

SUDOKU = readInputTxtFile() 
CELLS = createCell(SUDOKU)



def AC3(csp):
    
    """ 
    Uses the CSP or arc consistency to check each individual constraint.
    Returns False if an inconsistency is found within the constraints, 
    otherwise True
    
    """
    cell_queue = []
    for cell in CELLS.keys:
        cell_queue.append(CELLS[cell])

    return
    while queue:
        Xi,Xm = cell_queue.pop(0)

        if revise(SUDOKU, Xi, Xm):
    
            if len(Xi.domain) == 0:
                return False

            """ for Xk in csp.related_cells[xi]:
                    if Xk != xi:
                        queue.append((Xk, xi))
            Still trying to figure out what the related_cells function does
            """
    return True
    """ 
    If you can think of any possible ideas for what else we would need to check 
    inside of the AC3 algo, just leave it here
    """

        

    

def revise(SUDOKU, Xi, Xm):
    """
    Takes the current cell popped from the sudoku board, 
    makes a list of values from the domain of the cell.
    Checks each individual value in the domain with the constraints,
    if the constraints are false, it will remove this value from the domain.
    What is left is the viable options that can be chose at the specific cell
    for the algorithm to try with.
    """

    revised = False

    for dom in cell_queue[Xi]:
        if not any("constraints() in SUDOKU.domain[Xm]"):
            SUDOKU.domain[Xi].remove(dom)
            revised = True
    return revised

def best_val(SUDOKU, Xi):



return