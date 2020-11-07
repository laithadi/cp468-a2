from readingInput import readInputTxtFile
from cell import Cell

SUDOKU = readInputTxtFile()

def createCell(sudoku):
    """
    Create the constaint for each cell. 
    """

    all_cells = {}

    for r in range(0,9):
        for c in range(0,9):
            all_cells['cell'+str(r+1)+str(c+1)] = Cell(value=sudoku[r][c], index=(r,c))

    return all_cells
