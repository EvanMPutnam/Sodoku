def createBoard():
    '''
    Creates a basic structure for the game board.
    Does not fill with numbers yet.  Placeholders of "."
    :return:
    '''
    #Format is going to be x y value
    yArr = []
    for y in range(9):
        xArr = []
        for x in range(9):
            xArr.append(".")
        yArr.append(xArr)
    return yArr


def populateBoard(board, file):
    '''
    Input board from createBoard as well as a file
    :param board:
    :param file:
    :return:
    '''
    lst = []
    for line in open(file):
        ln = line.split()
        lst.append(ln)
    for y in range(9):
        for x in range(9):
            if(lst[y][x] != "0"):
                board[y][x] = int(lst[y][x])








def printBoard(board):
    '''
    Prints out the board in an easy to understand format
    :param board:
    :return:
    '''
    countY = 0
    for elem in board:
        countX = 0
        for el in elem:
            print(el, end=" ")
            countX += 1
            if countX%3 == 0 and countX != 9:
                print("#", end=" ")

        print("")
        countY += 1
        if(countY%3 == 0 and countY != 9):
            print("# "*11)



def solve(config):
    '''
    Solves the board that is given to it
    :param config:
    :return:
    '''
    coord = getNextCoord(config)
    #Base case
    if(coord == []):
        return True
    for i in range(1,10):
        if(checkConflict(coord[0], coord[1], i, config) == True):
            config[coord[1]][coord[0]] = i
            #Recursion
            if(solve(config) == True):
                return True
            else:
                config[coord[1]][coord[0]] = "."
    return False


def checkConflict(x, y, value, board):
    '''
    Checks to see if their is a conflict in the current board structure.
    Ex: diagonal, horizontal, within quadrant
    :param x:
    :param y:
    :param value:
    :param board:
    :return:
    '''
    if value in board[y]:
        return False
    else:
        for y2 in range(9):
            if value == board[y2][x]:
                return False

    quad = getQuadrand(x, y)
    lst = getElementsInQuadrant(board, quad)

    if value in lst:
        return False

    return True


def getQuadrand(x, y):
    '''
    Gets the quadrant of the given x and y coordinates
    :param x:
    :param y:
    :return:
    '''
    quadrand = 0
    if x>=6:
        if y>= 6:
            quadrand = 9
        elif y>=3:
            quadrand = 6
        else:
            quadrand = 3
    elif x>=3:
        if y >= 6:
            quadrand = 8
        elif y >= 3:
            quadrand = 5
        else:
            quadrand = 2
    else:
        if y >= 6:
            quadrand = 7
        elif y >= 3:
            quadrand = 4
        else:
            quadrand = 1
    return quadrand



def getElementsInQuadrant(board, quadrant):
    '''
    Get the elements of each quadrant
    :param board:
    :param quadrant:
    :return:
    '''
    locations = [(0,0), (3,0),(6,0), (0, 3), (3, 3),(6, 3),(0,6),(3,6),(6,6)]
    q = locations[quadrant-1]
    lst = []
    for y in range(0,3):
        for x in range(0,3):
            if(board[q[1]+y][q[0]+x] != "."):
                lst.append(board[q[1] + y][q[0] + x])

    return lst







def getNextCoord(board):
    '''
    Get the next empty coordinate set in the board
    :param board:
    :return:
    '''
    coords = []
    for y in range(9):
        for x in range(9):
            if(board[y][x] == "."):
                coords = [x, y]
                return coords
    return coords




def testSuite():
    '''
    Test suite for different sudoku puzzles.
    Structure of your own graphs are int 1-9 and then "." for empty space.
    Structure for the external graphs are 0 for empty space and 1-9 for regular space.
    External graph values seperated by space like so...

    Contents of some_file.txt
    0 5 0 9 0 0 0 0 1
    0 0 0 0 1 0 0 7 2
    0 0 1 0 0 0 0 0 9
    0 0 7 8 9 0 0 3 0
    0 0 3 2 0 7 5 0 0
    0 2 0 0 6 5 1 0 0
    9 0 0 0 0 0 4 0 0
    6 1 0 0 2 0 0 0 0
    7 0 0 0 0 8 0 2 0


    You can then solve this graph with this code...

    sudok = createBoard()
    populateBoard(sudok, "some_file.txt")
    solve(sudok)
    printBoard(sudok)

    :return:
    '''

    grid2 =[[3,".",6,5,".",8,4,".","."],
          [5,2,".",".",".",".",".",".","."],
          [".",8,7,".",".",".",".",3,1],
          [".",".",3,".",1,".",".",8,"."],
          [9,".",".",8,6,3,".",".",5],
          [".",5,".",".",9,".",6,".","."],
          [1,3,".",".",".",".",2,5,"."],
          [".",".",".",".",".",".",".",7,4],
          [".",".",5,2,".",6,3,".","."]]
    printBoard(grid2)
    print()
    print(solve(grid2))
    print()
    printBoard(grid2)

    print("---------------------------------------------")
    grid3 = [[2, 5, 7, ".", 6, ".", ".", ".", 4],
             [".", ".", 3, ".", ".", ".", ".", ".", "."],
             [".", 1, ".", ".", 9, 4, ".", 3, 2],
             [".", ".", ".", 2, 8, ".", ".", ".", "."],
             [5, ".", ".", ".", ".", ".", ".", ".", 6],
             [".", ".", ".", ".", 3, 1, ".", ".", "."],
             [1, 6, ".", 8, 5, ".", ".", 2, "."],
             [".", ".", ".", ".", ".", ".", 1, ".", "."],
             [3, ".", ".", ".", 1, ".", 6, 9, 5]]
    printBoard(grid3)
    print()
    print(solve(grid3))
    print()
    printBoard(grid3)

    print("---------------------------------------------")
    #Getting from a board and then displaying
    b1 = createBoard()
    populateBoard(b1, input("Enter text File: "))
    printBoard(b1)
    print()
    print(solve(b1))
    print()
    printBoard(b1)


if __name__ == '__main__':
    testSuite()

