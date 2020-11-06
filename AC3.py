from readingInput import readInputTxtFile
from temp import createCell  

SUDOKU = readInputTxtFile() 
CELLS = createCell(SUDOKU)


def AC3(csp):
    
    """ 
    Uses the CSP or arc consistency to check each individual constraint.
    Returns False if an inconsistency is found within the constraints, 
    otherwise True
    
    """

    