def readInputTxtFile():

    f = open("input.txt", "r")
    lines = f.readlines()

    sudoku = ''

    for line in lines:
        temp = line.split(',')
        sudoku += str(temp)

    return sudoku