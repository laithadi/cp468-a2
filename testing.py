from AC3 import AC3
from backtrack import backtrackCSP
from constraints import CSP
from temp import SUDOKU

def solve(grid, index, total):
    
    print("\nSudoku {}/{} : \n{}".format(index, total, print_grid(grid)))


    print("{}/{} : AC3 starting".format(index, total))


    # instanciate Sudoku
    cons = Sudoku(grid)

    # launch AC-3 algorithm of it
    AC3_result = AC3(cons)

    # Sudoku has no solution
    if not AC3_result:
        print("{}/{} : this sudoku has no solution".format(index, total))

    else:
        
        # check if AC-3 algorithm has solve the Sudoku
        if cons.isFinished():

            print("{}/{} : AC3 was enough to solve this sudoku !".format(index,total))
            print("{}/{} : Result: \n{}".format(index, total, cons))

        # continue the resolution
        else:

            print("{}/{} : AC3 finished, Backtracking starting...".format(index,total))

            assignment = {}

            # for the already known values
            for cell in cons.cells:

                if len(cons.possibilities[cell]) == 1:
                    assignment[cell] = cons.possibilities[cell][0]
            
            # start backtracking
            assignment = backtrackCSP(assignment, cons)
            
            # merge the computed values for the cells at one place
            for cell in cons.possibilities:
                cons.possibilities[cell] = assignment[cell] if len(cell) > 1 else cons.possibilities[cell]
            
            if assignment:
                print("{}/{} : Result: \n{}".format(index, total, cons))

            else:
                print("{}/{} : No solution exists".format(index, total))