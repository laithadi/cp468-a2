from AC3 import AC3
from backtrack import backtrackCSP
from constraints import CSP
from temp import SUDOKU

def main():


    cons = CSP(Sudoku)
    result = AC3(cons)

    if result is True:
        #for cells in cons.cells:
            
    else:
        answer = {}

        for cell in cons.cells:
            if len(cons.possibilities) == 1:
                answer[cell] = cons.possibilities[cell]
        answer = backtrackCSP(answer, cons)

        for cell in cons.possibilities:
            if len(cell) > 1:
                cons.possibilities[cell] = answer[cell]
            else:
                cons.possibilities[cell]

        if answer == True:
            return "print table"
        else:
            return "not solvable"