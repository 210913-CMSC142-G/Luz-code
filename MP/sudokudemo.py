# A Compilation of 3 Algorithms to Solve Sudoku
# Submitted by: Luz Dungo (CS 142 - G)

# Libraries
from operator import index
from random import choices, randint
from math import sqrt
import sys
from functools import reduce
from time import perf_counter
from constraint import *
import numpy

## Run using 'python sudokudemo.py <name of txt file> <method>'

## TODO: include comments
## TODO: make GUI
## TODO: display all solutions in constraint programming

############# STOCHASTIC SEARCH

GENERATION_SIZE = 10
BRANCHING_FACTOR = 4

def heuristic_s(board, gridsize = 9, blocksize = 3):
    collisions = 0
    for i in range(gridsize):
        for j in range(gridsize):
            val = board[i][j]
            for n in range(gridsize):
                if n != i and board[n][j] == val:
                    collisions += 1
            for m in range(gridsize):
                if m != j and board[i][m] == val:
                    collisions += 1
            squareX = j // blocksize
            squareY = i // blocksize
            for n in range(blocksize):
                for m in range(blocksize):
                    if not (blocksize * squareX + m == j or blocksize * squareY + n == i) and board[blocksize * squareY + n][blocksize * squareX + m] == val:
                        collisions += 1
    return collisions

def deepcopy_board_s(board):
    ret = []
    for row in board:
        ret_row = []
        for elem in row:
            ret_row.append(elem)
        ret.append(ret_row)
    return ret

def generate_successor_s(board, size, fixed):
    choices = [[y for y in x[1] if (x[0], y) not in fixed] for x in enumerate([list(range(size)) for x in range(size)])]
    row = randint(0, size - 1)
    index1 = randint(0, len(choices[row]) - 1)
    choice1 = choices[row][index1]
    del choices[row][index1]
    index2 = randint(0, len(choices[row]) - 1)
    choice2 = choices[row][index2]
    del choices[row][index2]
    ret = deepcopy_board_s(board)
    ret[row][choice2], ret[row][choice1] = ret[row][choice1], ret[row][choice2]
    return ret

def generate_board_s(original_board, size, fixed):
    board = deepcopy_board_s(original_board)
    choices = [[y for y in range(1, size + 1) if y not in x] for x in original_board]
    for i in range(size):
        for j in range(size):
            if (i, j) not in fixed:
                index = randint(0, len(choices[i]) - 1)
                board[i][j] = choices[i][index]
                del choices[i][index]
    return board

def solver_s(size = 9):
    if len(sys.argv) > 1:
        fileName = sys.argv[1].upper()
    else:
        print("No input puzzle given")
        exit()
    board = open(fileName).read()
    board = [ int(i) for i in board.split() ]
    board = [board[i * 9: (i + 1) * 9] for i in range((len(board) + 9 - 1) // 9)]
    original_board = board
    fixed_values = set([])
    for i in range(size):
        for j in range(size):
            if original_board[i][j] != 0:
                fixed_values.add((i, j))
    solved = False
    solution = None
    boards = []
    for i in range(GENERATION_SIZE):
        board = generate_board_s(original_board, size, fixed_values)
        boards.append(board)
    boards = [(heuristic_s(board, gridsize=size, blocksize=int(sqrt(size))), board) for board in boards]
    lowest = 0
    m = 1
    while not solved:
        boards.sort(key = lambda x: x[0])
        lowest_ = boards[0][0]
        if lowest_ == lowest:
            m = m + 1
        else:
            m = 1
        lowest = lowest_
        if m > 40:
            print("Local minimum")
            solver_s()
            exit()
        boards = boards[:GENERATION_SIZE]
        if boards[0][0] == 0:
            solved = True
            solution = boards[0][1]
            print_board_b(solution)
        else:
            successors = []
            for board in boards:
                for i in range(BRANCHING_FACTOR):
                    successors.append(generate_successor_s(board[1], size, fixed_values))
                for s in successors:
                    boards.append((heuristic_s(s, gridsize=size, blocksize=int(sqrt(size))), s))
    return solution
    

############# BACKTRACKING

def solve_b(bo):
    find = find_empty_b(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid_b(bo, i, (row, col)):
            bo[row][col] = i
            if solve_b(bo):
                return True
            bo[row][col] = 0
    return False

def valid_b(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def print_board_b(bo):
    for i in range(len(bo)):
        if i % 3 == 0:
            if i == 0:
                print (" ┎─────────────────────────────┒")
            else:
                print(" ┠─────────────────────────────┨")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" ┃ ", end=" ")
            if j == 8:
                print(bo[i][j], " ┃")
            else:
                print(str(bo[i][j]), end=" ")
    print(" ┖─────────────────────────────┚")

def find_empty_b(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

############# CONSTRAINT PROGRAMMING
# Normalizes sudoku puzzle
def dataNormalize_c(data):
    """
    args: data; output from sudoku_solve
    returns: Normalized output of input
    """
    sudoku_nums = [ eachPos[1] for eachPos in sorted( data[0].items() ) ]
    sudoku = []
    for step in range(0, 81, 9):
        sudoku.append(sudoku_nums[step: step + 9])
    print_board_b(sudoku)

# Solves the sudoku puzzle
def sudoku_solve_c():
    """
    args: None
    returns: Sudoku solution
    return type: list
    description:
        * It reads sudoku puzzle via input text file.
        * Creates problem instance, sudoku = Problem()
        * Adds sudoku input and their indices as variables
        * Adds constraints to the problem
            1. No two number in a row should be the same
            2. No two numbers in a column should be the same
            3. No two numbers in a 3x3 box shold be the same
        * Returns teh solution
    """
    # reads the puzzle from file
    if len(sys.argv) > 1:
        fileName = sys.argv[1].upper()
    puzzleNums = open(fileName).read()
    # stores the numbers in a list. Ex: [1, 2, 9, 0, 3, ...]
    puzzleNums = [ int (eachNum) for eachNum in puzzleNums.split() ]
    ## Problem instance created.
    ## Recursive backtracking is used here    
    sudoku = Problem( RecursiveBacktrackingSolver() )
    ## List of 9x9 sudoku puzzle indices. Ex: [(0, 0), (0, 1), ... , (9, 9)]
    sudokuIndex = [ (row, col) for row in range(9) for col in range(9) ]
    # adding variables to the sudoku instance
    for eachIndex, eachNum in zip(sudokuIndex, puzzleNums):
        # if empty location is found, its range is set to 1-10
        if eachNum == 0:
            sudoku.addVariable(eachIndex, range(1, 10))
        # if not an empty location, its value is assigned
        else:
            sudoku.addVariable(eachIndex, [eachNum])
    
    ## Constraints for each row and column
    # counting from 0-9 (number of rows/columns)
    var = 0
    for aCount in range(9):
        ## A list of locations present in a row
        rowIndices = [ (var, col) for col in range(9) ]
        ## Adding constraint
        # no two numbers in a row should be the same
        sudoku.addConstraint( AllDifferentConstraint(), rowIndices )
        ## A list of locations present in a column
        colIndices = [ (row, var) for row in range(9) ]
        ## Adding constraint
        # no two numbers in a column should be the same
        sudoku.addConstraint( AllDifferentConstraint(), colIndices )
        var += 1
    
    ## Constraints for each block (3x3) of the board
    # finding all boxes in sudoku board (9 in this case)
    rowStep = 0
    colStep = 0
    while rowStep < 9:
        colStep = 0
        while colStep < 9:
            ## List of locations present in a box
            boxIndices = [ (row, col) for row in range(rowStep, rowStep + 3) for col in range(colStep, colStep + 3) ]
            ## Adding constraint
            # no two numbers in a box should be the same
            sudoku.addConstraint( AllDifferentConstraint(), boxIndices )
            colStep += 3
        rowStep += 3
    # return the solution
    return sudoku.getSolutions()



############# MAIN
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) > 1:
            fileName = sys.argv[1].upper()
        else:
            print("No input puzzle given")
            exit()
        timeA1 = perf_counter()
        board = open(fileName).read()
        board = [ int (i) for i in board.split() ]
        board = [board[i * 9: (i + 1) * 9] for i in range((len(board) + 9 - 1) // 9)]
        print("\n          BACKTRACKING")
        if solve_b(board):
            print_board_b(board)
        else:
            print("No solution found")
            exit()
        timeA2 = perf_counter()
        print(f'TIME TAKEN : {round(timeA2-timeA1,3)} SECONDS')

        print("---------------------------------")

        print("\n\tSTOCHASTIC SEARCH")
        timeB1 = perf_counter()
        solver_s()
        timeB2 = perf_counter()
        print(f'TIME TAKEN : {round(timeB2-timeB1,3)} SECONDS')

        print("---------------------------------")
        
        print("\n     CONSTRAINT PROGRAMMING")
        timeC1 = perf_counter()
        dataNormalize_c( sudoku_solve_c() )
        timeC2 = perf_counter()
        print(f'TIME TAKEN : {round(timeC2-timeC1,3)} SECONDS')
        
    else:
        print("No input puzzle given")