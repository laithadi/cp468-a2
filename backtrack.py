from readingInput import readInputTxtFile
from temp import createCell  
from cell import Cell
from constraints import CSP
from helper import constraint_check, assign, unassign

def backtrackCSP(answer, CSP):
    
    """
    Instantly checks if the length of our answer is equivalent to the
    amount of cells in SUDOKU, if true we have solved the puzzle
    """

    if len(answer) == len(CSP.cells):
        return answer

    # If not solved, we have to now choose a cell to test
    cell = select_variable(answer, CSP)
    for val in order_values(CSP, cell):
        if constraint_check(CSP, answer, cell, val):
            assign(CSP, cell, val, answer)
            result = backtrackCSP(answer, CSP)

            if result == True:
                return result
            
            unassign(CSP, cell, answer)


    return False


def select_variable(answer, CSP):
    unchosen = []

    for cell in CSP.cells:
        if cell not in answer:
            unchosen.append(cell)
    return unchosen

def order_values(CSP, cell):
    if len(CSP.possibilities) == 1:
        return CSP.possibilities[cell]
    else:
        values = CSP.possibilities[cell]

        return values[0]