#backtracking 6x6 
def print_sudoku(sudoku):
    """
    Prints the Sudoku puzzle in a 6x6 grid format
    """
    for i in range(6):
        if i % 2 == 0:
            print("+-------+-------+")
        for j in range(6):
            if j % 2 == 0:
                print("|", end=" ")
            print(sudoku[i][j], end=" ")
        print("|")
    print("+-------+-------+")

def is_valid(sudoku, row, col, num):
    """
    Returns True if the given number can be placed in the given cell
    without violating the Sudoku rules
    """
    # Check if the number is already in the same row or column
    for i in range(6):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False
    # Check if the number is already in the same 2x3 box
    box_row = (row // 2) * 2
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 2):
        for j in range(box_col, box_col + 3):
            if sudoku[i][j] == num:
                return False
    return True

def solve_sudoku(sudoku):
    """
    Solves the Sudoku puzzle using backtracking
    """
    for row in range(6):
        for col in range(6):
            if sudoku[row][col] == 0:
                for num in range(1, 7):
                    if is_valid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True

# Example puzzle
puzzle = [
    [0, 2, 3, 1, 6, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 5, 6, 2, 3, 0],
	[0, 0, 1, 5, 0, 0],
	[3, 0, 0, 0, 0, 2],
]

print("Puzzle:")
print_sudoku(puzzle)

if solve_sudoku(puzzle):
    print("\nSolution:")
    print_sudoku(puzzle)
else:
    print("No solution found.")
