#Bitmask 4x4
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

def get_candidates(sudoku, row, col):
    """
    Returns a bit mask representing the possible candidates for the given cell
    """
    candidates = 0b1111
    for i in range(4):
        candidates &= ~(1 << sudoku[i][col])  # remove numbers already in the same column
        candidates &= ~(1 << sudoku[row][i])  # remove numbers already in the same row
    for i in range(row // 2 * 2, row // 2 * 2 + 2):
        for j in range(col // 2 * 2, col // 2 * 2 + 2):
            candidates &= ~(1 << sudoku[i][j])  # remove numbers already in the same box
    return candidates

def solve_sudoku(sudoku, row=0, col=0):
    """
    Solves the Sudoku puzzle using bit masks
    """
    if row == 4:
        return True
    next_row = row if col < 3 else row + 1
    next_col = (col + 1) % 4
    if sudoku[row][col] != 0:
        return solve_sudoku(sudoku, next_row, next_col)
    candidates = get_candidates(sudoku, row, col)
    for num in range(1, 5):
        if candidates & (1 << num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku, next_row, next_col):
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
