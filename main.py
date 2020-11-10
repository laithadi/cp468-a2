from AC3 import AC3
from backtrack import backtrackCSP
from constraints import CSP
from helper import readInputTxtFile

SUDOKU = readInputTxtFile()

def solve(sudoku):
    print("The starting sudoku table \n")
    i = 0
    for char in sudoku:
        print(char + '  ', end='')
        i += 1
        if i % 9 == 0:
            print()

    print("\n")
    
    
    cons = CSP(sudoku)
    AC3_result = AC3(cons)

    if not AC3_result:
        print("AC3 can not solve")

    else:

        if cons.completed():
            print("COMPLETED")

        else:
        
            answer = {}
            for cell in cons.cells:
                if len(cons.possibilities[cell]) == 1:
                    answer[cell] = cons.possibilities[cell][0]
            
            answer = backtrackCSP(answer, cons)
            
            for cell in cons.possibilities:
                cons.possibilities[cell] = answer[cell] if len(cell) > 1 else cons.possibilities[cell]
            
            if answer:
                print("Solved Puzzle:")
                i = 0
                for coord in answer:
                    print(str(answer[coord]) + '  ', end='')
                    i += 1
                    if i % 9 == 0:
                        print()

            else:
                print("No solution")


solve(SUDOKU)