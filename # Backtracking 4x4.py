# Backtracking 4x4
def print_sudoku(sudoku):
    """
    Prints the Sudoku puzzle in a 4x4 grid format
    """
    for i in range(4):
        if i % 2 == 0:
            print("+ - - + - - +")
        for j in range(4):
            if j % 2 == 0:
                print("|", end=" ")
            print(sudoku[i][j], end=" ")
        print("|")
    print("+ - - + - - +")

def find_empty(sudoku):
    """
    Returns the row and column of an empty cell in the Sudoku puzzle
    """
    for i in range(4):
        for j in range(4):
            if sudoku[i][j] == 0:
                return i, j
    return None

def is_valid(sudoku, num, row, col):
    """
    Returns True if the given number is valid in the given cell in the Sudoku puzzle
    """
    for i in range(4):
        if sudoku[i][col] == num:
            return False
        if sudoku[row][i] == num:
            return False
    box_row = (row // 2) * 2
    box_col = (col // 2) * 2
    for i in range(box_row, box_row + 2):
        for j in range(box_col, box_col + 2):
            if sudoku[i][j] == num:
                return False
    return True

def solve_sudoku(sudoku):
    """
    Solves the Sudoku puzzle using backtracking
    """
    empty_cell = find_empty(sudoku)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 5):
        if is_valid(sudoku, num, row, col):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0
    return False

# Example usage
sudoku = [[0, 0, 0, 3],
	[0, 4, 0, 0],
	[0, 0, 3, 2],
	[0, 0, 0, 0]]

print("Sudoku puzzle:")
print_sudoku(sudoku)

if solve_sudoku(sudoku):
    print("Solution:")
    print_sudoku(sudoku)
else:
    print("No solution exists.")
