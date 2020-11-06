BOX1 = [(0,0),(0,1),(0,2),
        (1,0),(1,1),()] 


def row_con(cells, cell, di):
    
    cell_r = cell.index[0]
    cell_c = cell.index[1]
    cell_v = cell.value

    for n_cell in cells:
        if n_cell.index[0] == cell_r and n_cell.index[1] != cell_c:
            if n_cell.value == cell_v:
                return False  

    return True 


def col_con(cells, cell, di):
    
    cell_r = cell.index[0]
    cell_c = cell.index[1]
    cell_v = cell.value

    for n_cell in cells:
        if n_cell.index[1] == cell_c and n_cell.index[0] != cell_r:
            if n_cell.value == cell_v:
                return False 
    
    return True 



def box_con(cells, cell, di):
    
    return True 



def constraints(cells, cell, di):

    if (not row_con(cells, cell, di)) or (not col_con(cells, cell, di)) or (not box_con(cells, cell, di)): return False

    return True 


























def c1on_rows(cells):

    for cell in cells:
        
        row = cells[cell].index[0]
        col = cells[cell].index[1]

        for i in range(0,9):
            if i != col:
                if cells[cell].value == cells['cell'+str(row+1)+str(i+1)].value:
                    return False

    return True 


def c1on_cols(cells):

    for cell in cells:

        row = cells[cell].index[0]
        col = cells[cell].index[1]

        for i in range(0,9):
            if i != row:
                if cells[cell].value == cells['cell'+str(i+1)+str(col+1)]:
                    return False
    
    return True






# def con_box(cells):

#     for cell in cells:

#         row = cells[cell].index[0]
#         col = cells[cell].index[1]

#         norm_row = row % 3 
#         norm_col = col % 3

#         if norm_row == 0:
#             for newrow in range(1,3):

#                 if cells[cell].value == cells['cell'+str(row+newrow+1)+str(col+1)]: # checks value straight below cell 
#                     return False 

#                 if norm_col == 0: 
#                     for newcol in range(1,3):

#                         if cells[cell].value == cells['cell'+str(row+1)+str(col+newcol+1)]: # checks value straight to the right 
#                             return False

#                         if cells[cell].value == cells['cell'+str(row+newrow+1)+str(col+newcol+1)]:
#                             return False 

#                 if norm_col == 1:

#                     if cells[cell].value == cells['cell'+str(row+1)+str(col+1+1)]: # checks value straight to the right 
#                             return False

#                     if cells[cell].value == cells['cell'+str(row+1)+str(col+1-1)]: # checks value straight to the right 
#                             return False

#                     if cells[cell].value == cells['cell'+str(row+newrow+1)+str(col+1+1)]: # checks value straight to the right 
#                             return False

#                     if cells[cell].value == cells['cell'+str(row+newrow+1)+str(col+1-1)]: # checks value straight to the right 
#                             return False


#                 if norm_col == 2:

#                     pass
    
#     return True 