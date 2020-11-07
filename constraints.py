BOX1 = [(0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1), (2,2)] 

BOX2 = [(0,3),(0,4),(0,5),
        (1,3),(1,4),(1,5),
        (2,3),(2,4), (2,5)] 

BOX3 = [(0,6),(0,7),(0,8),
        (1,6),(1,7),(1,8),
        (2,6),(2,7), (2,8)] 

BOX4 = [(3,0),(3,1),(3,2),
        (4,0),(4,1),(4,2),
        (5,0),(5,1), (5,2)] 

BOX5 = [(3,3),(3,4),(3,5),
        (4,3),(4,4),(4,5),
        (5,3),(5,4), (5,5)] 

BOX6 = [(3,6),(3,7),(3,8),
        (4,6),(4,7),(4,8),
        (5,6),(5,7), (5,8)]

BOX7 = [(6,0),(6,1),(6,2),
        (7,0),(7,1),(7,2),
        (8,0),(8,1), (8,2)] 

BOX8 = [(6,3),(6,4),(6,5),
        (7,3),(7,4),(7,5),
        (8,3),(8,4), (8,5)] 
 
BOX9 = [(6,6),(6,7),(6,8),
        (7,6),(7,7),(7,8),
        (8,6),(8,7), (8,8)] 


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



def check_box(cells, cell, di, box):

    for n_cell in cells:
        if n_cell.index in box:
            if n_cell.value == cell.value:
                return False 

    return True 


def box_con(cells, cell, di):
    
    if cell.index in BOX1:
        return check_box(cells, cell, di, BOX1)
    
    if cell.index in BOX2:
        return check_box(cells, cell, di, BOX2)

    if cell.index in BOX3:
        return check_box(cells, cell, di, BOX3)

    if cell.index in BOX4:
        return check_box(cells, cell, di, BOX4)

    if cell.index in BOX5:
        return check_box(cells, cell, di, BOX5)

    if cell.index in BOX6:
        return check_box(cells, cell, di, BOX6)

    if cell.index in BOX7:
        return check_box(cells, cell, di, BOX7)

    if cell.index in BOX8:
        return check_box(cells, cell, di, BOX8)

    if cell.index in BOX9:
        return check_box(cells, cell, di, BOX9)


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