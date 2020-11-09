from readingInput import readInputTxtFile
from temp import createCell  
from cell import Cell
from constraints import constraints


def backtrackCSP(answer, SUDOKU):
    
    """
    Instantly checks if the length of our answer is equivalent to the
    amount of cells in SUDOKU, if true we have solved the puzzle
    """

    if len(answer) == len("new name"):
        return answer

    # If not solved, we have to now choose a cell to test
    cell = select_variable(answer, SUDOKU)
    for val in domain_ordered("New name", cell):
        if "name for no constraints function"("new name", answer, val):
            "new name for assign"("newname", cell, val, answer)
            result = backtrackCSP(answer, "newname")

            if result == True:
                return result
            
            "new name for unassign"("newname", cell, answer)


return False


def select_variable(answer, "newname"):
    unchosen = []

    for cell in "newname".cells:
        if cell not in answer:
            unchosen.append(cell)
    return unchosen

def order_values("newname", cell):
    if len("newname".possibilites) == 1
        return "newname".possibilites[cell]
    else:
        return "newname".possibilites[cell]