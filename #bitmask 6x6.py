#bitmask 6x6
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

def is_valid(mask, row, col, num):
    """
    Returns True if the given number can be placed in the given cell
    without violating the Sudoku rules
    """
    # Check if the number is already in the same row, column or 2x3 box
    return not (mask[row] & (1 << num) or
                mask[6 + col] & (1 << num) or
                mask[12 + (row//2)*2 + col//3] & (1 << num))

def set_bit(mask, row, col, num):
    """
    Sets the bit corresponding to the given number in the masks
    for the given row, column and 2x3 box
    """
    mask[row] |= (1 << num)
    mask[6 + col] |= (1 << num)
    mask[12 + (row//2)*2 + col//3] |= (1 << num)

def clear_bit(mask, row, col, num):
    """
    Clears the bit corresponding to the given number in the masks
    for the given row, column and 2x3 box
    """
    mask[row] &= ~(1 << num)
    mask[6 + col] &= ~(1 << num)
    mask[12 + (row//2)*2 + col//3] &= ~(1 << num)

def solve_sudoku(sudoku, mask, row=0, col=0):
    """
    Solves the Sudoku puzzle using bitmasks
    """
    if row == 6:
        return True

    next_row = row if col < 5 else row + 1
    next_col = (col + 1) % 6

    if sudoku[row][col] != 0:
        return solve_sudoku(sudoku, mask, next_row, next_col)

    for num in range(1, 7):
        if is_valid(mask, row, col, num):
            sudoku[row][col] = num
            set_bit(mask, row, col, num)
            if solve_sudoku(sudoku, mask, next_row, next_col):
                return True
            sudoku[row][col] = 0
            clear_bit(mask, row, col, num)

    return False

# Example puzzle
puzzle = [[0, 2, 3, 1, 6, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 5, 6, 2, 3, 0],
	[0, 0, 1, 5, 0, 0],
	[3, 0, 0, 0, 0, 2]
]

mask = [0] * 18  # 3 masks of size 6

print("Puzzle:")
print_sudoku(puzzle)

if solve_sudoku(puzzle, mask):
    print("\nSolution:")
    print_sudoku(puzzle)
else:
    print("No solution found.")
