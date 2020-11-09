import itertools

COLUMNS = "ABCDEFGHI"
ROWS = "123456789"


class CSP:

    def __init__(self, sudoku):

        game = list(sudoku)

        self.cells = list() 
        self.domains = dict()
        self.b_constraints = list() 
        self.neighbour_cells = dict() 
        self.pruned = dict()

        self.cells = self.create_coords()
        self.possibilities = self.create_domain(sudoku)  
        constraints = self.create_constraints()
        self.b_constraints = self.create_b_constraints(constraints)
        self.neighbour_cells = self.create_neighbours()
        self.pruned = {v: list() if sudoku[i] == '-' else [int(sudoku[i])] for i, v in enumerate(self.cells)}



    def completed(self):

        for c, p in self.possibilities.items():
            if len(p) > 1:
                return False 

        return True 
    

    def create_coords(self):

        coords_all_cells = [] 

        for letter in COLUMNS: 
            for num in ROWS:
                temp = letter + num 
                coords_all_cells.append(temp)

        return coords_all_cells
    

    def create_domain(self, sudoku):

        ls_sudoku = list(sudoku)

        poss = {} 

        for ind, coord in enumerate(self.cells):

            if ls_sudoku[ind] == '-':
                poss[coord] = [1,2,3,4,5,6,7,8,9]

            else:
                poss[coord] = [int(ls_sudoku[ind])]

        return poss

    
    def create_constraints(self):

        con_row, con_col, con_box = [],[],[] 

        for num in ROWS:
            con_row.append([letter + num for letter in COLUMNS])

        for letter in COLUMNS:
            con_col.append([letter + num for num in ROWS])
        
        square_r = list(COLUMNS[i:i+3] for i in range(0, len(ROWS), 3))
        square_c = list(ROWS[i:i+3] for i in range(0, len(COLUMNS), 3))

        for row in square_r:
            for col in square_c:

                square_con = []

                for i in row:
                    for j in col:

                        square_con.append(i+j)

                con_box.append(square_con)

        return con_row + con_col + con_box        


    def create_b_constraints(self, constraints):

        con_binary = [] 

        for constraint in constraints:

            temp = [] 

            for c in itertools.permutations(constraint, 2):
                temp.append(c) 
            
            for b_c in temp:
                ls_con = list(b_c)

                if ls_con not in con_binary:
                    con_binary.append([b_c[0], b_c[1]])
        
        return con_binary

    
    def create_neighbours(self):

        neighbors = {} 

        for cell in self.cells:
            neighbors[cell] = [] 
            for con in self.b_constraints:
                if cell == con:
                    neighbors[cell].append(con[1])

        return neighbors

    def __str__(self):
        s = ''
        n = 0
        for cell in self.cells:
            s = s + self.cells[n] + ' '
            n += 1
            if n % 9 == 0:
                s += '\n'
        return s