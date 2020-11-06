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












# def getInputInd():
#     """
#     returns a tuple of indices (i,j) for cells with a given value from input.txt 
#     """
#     pass

# def getRows(index):
#     """
#     returns a tuple with the indices (i,j) in the same row as the argument -- index.
#     """
#     pass 

# def getCol(index):
#     """
#     returns a tuple with the indices (i,j) in the same column as the argument -- index.
#     """
#     pass 

# def getBox(index):
#     """
#     returns a tuple with the indices (i,j) in the same box as the argument -- index.
#     """
#     pass 

# def updatesDomain(index):
#     #get the valye of index
#     # call the getrows 
#     # getcol
#     # getbox 
#     #for loop that goes to all the above indices and calls cell.con[] == 0
#     pass    

# def check_con_one():
#     """
#     checks for all constraints and sees which constraints has one 1 in it. we call cell.vailable_vals
#     """
#     pass
    
