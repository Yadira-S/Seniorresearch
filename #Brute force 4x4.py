#Brute force 4x4
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

def is_valid(sudoku):
    """
    Returns True if the Sudoku puzzle is valid
    """
    for i in range(4):
        row = [sudoku[i][j] for j in range(4)]
        col = [sudoku[j][i] for j in range(4)]
        if len(set(row)) != 4 or len(set(col)) != 4:
            return False
    for i in range(0, 4, 2):
        for j in range(0, 4, 2):
            box = [sudoku[m][n] for m in range(i, i+2) for n in range(j, j+2)]
            if len(set(box)) != 4:
                return False
    return True

def solve_sudoku(sudoku, row=0, col=0):
    """
    Solves the Sudoku puzzle using brute-force
    """
    if row == 4:
        return is_valid(sudoku)
    next_row = row if col < 3 else row + 1
    next_col = (col + 1) % 4
    if sudoku[row][col] != 0:
        return solve_sudoku(sudoku, next_row, next_col)
    for num in range(1, 5):
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
