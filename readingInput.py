def readInputTxtFile():

    f = open("input.txt", "r")
    
    sudoku = f.read().replace(',', '')

    return sudoku

