from readingInput import readInputTxtFile
from temp import createCell  
from cell import Cell
from constraints import constraints


def backtrackCSP(answer, SUDOKU):
    
    """
    Instantly checks if the length of our answer is equivalent to the
    amount of cells in SUDOKU, if true we have solved the puzzle
    """

    if len(answer)== len(SUDOKU):
        return answer

    # If not solved, we have to now choose a cell to test
    cell = select_variable(answer, SUDOKU)


return


def select_variable(assignment, SUDOKU):
    pos_cell = []


    for x not in SUDOKU.cells:
        if x not in assignment:
            pos_cell.append(x)

    return (pos_cell)

def one_val(SUDOKU, CELL):
    if len(Cell.domain) == 1:
        return cell.domain[1]


