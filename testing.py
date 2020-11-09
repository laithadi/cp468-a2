from AC3 import AC3
from backtrack import backtrackCSP
from constraints import CSP
from readingInput import readInputTxtFile

SUDOKU = readInputTxtFile()

def solve(sudoku):
    
    # print("\nSudoku {}/{} : \n".format(index, total))

    # PRINT THE START OF THE SUDOKU 


    # print("{}/{} : AC3 starting".format(index, total))


    # instanciate Sudoku
    print(sudoku)
    cons = CSP(sudoku)
    print(cons)

    # launch AC-3 algorithm of it
    AC3_result = AC3(cons)

    # Sudoku has no solution
    if not AC3_result:
        # print("{}/{} : this sudoku has no solution".format(index, total))
        print("errorrrrrrrrrr")

    else:
        
        # check if AC-3 algorithm has solve the Sudoku
        if cons.completed():

            # print("{}/{} : AC3 was enough to solve this sudoku !".format(index,total))
             
            # print("{}/{} : Result: \n{}".format(index, total, cons))
            print("COMPLETED")

        # continue the resolution
        else:

            # print("{}/{} : AC3 finished, Backtracking starting...".format(index,total))
            

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
                # print("{}/{} : Result: \n{}".format(index, total, cons))
                # SOLVED PRINT OUT THE RESULT SUDOKU HEREEEEE
                print("wbalabalf")

            else:
                # print("{}/{} : No solution exists".format(index, total))
                print("hithere")


solve(SUDOKU)