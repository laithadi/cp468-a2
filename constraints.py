from readingInput import readInputTxtFile
from temp import createCell  

SUDOKU = readInputTxtFile() 

CELLS = createCell(SUDOKU)

def con_rows(cells):

    for cell in cells:
        
        row = cells[cell].index[0]
        col = cells[cell].index[1]

        for i in range(0,9):
            if i != col:
                if cells[cell].value == cells['cell'+str(row+1)+str(i+1)].value:
                    return False

    return True 


def con_cols(cells):

    for cell in cells:

        row = cells[cell].index[0]
        col = cells[cell].index[1]

        for i in range(0,9):
            if i != row:
                if cells[cell].value == cells['cell'+str(i+1)+str(col+1)]:
                    return False
    
    return True


def con_box(cells):

    for cell in cells:

        row = cells[cell].index[0]
        col = cells[cell].index[1]

        norm_row = row % 3 
        norm_col = col % 3

        if norm_row == 0:
            for newrow in range(1,3):

                if cells[cell].value == cells['cell'+str(row+newrow+1)+str(col+1)]: # checks value straight below cell 
                    return False 

                if norm_col == 0: 
                    for newcol in range(1,3):

                        if cells[cell].value == cells['cell'+str(row+1)+str(col+newcol+1)]: # checks value straight to the right 
                            return False

                        if cells[cell].value == cells['cell'+str(row+newrow+1)+str(col+newcol+1)]:
                            return False 

                if norm_col == 1:

                    if cells[cell].value == cells['cell'+str(row+1)+str(col+1+1)]: # checks value straight to the right 
                            return False

                    if cells[cell].value == cells['cell'+str(row+1)+str(col+1-1)]: # checks value straight to the right 
                            return False

                    if cells[cell].value == cells['cell'+str(row+newrow+1)+str(col+1+1)]: # checks value straight to the right 
                            return False

                    if cells[cell].value == cells['cell'+str(row+newrow+1)+str(col+1-1)]: # checks value straight to the right 
                            return False


                if norm_col == 2:

                    pass
    
    return True 