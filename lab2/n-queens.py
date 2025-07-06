def print_solution(board):
    n = len(board)
    # ✅ Added visual borders for better UI
    border = "+" + "---+" * n
    for row in board:
        print(border)
        # ✅ Replaced '.' and 'Q' with formatted cells
        print("|" + "|".join(" Q " if col else "   " for col in row) + "|")
    print(border)
    print()

def is_safe(board, row, col, n):
    # Same as original: checking vertical and diagonals
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # ✅ Copied board correctly to avoid mutation issues
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# ✅ Loop for multiple N values (4 to 8)
for n in range(4, 9):
    # ✅ Improved header for visual clarity
    print(f"\n========== {n}-Queens Solutions ==========")
    
    all_solutions = solve_n_queens(n)
    
    # ✅ Separate and clear display of total number of solutions
    print(f"Total solutions: {len(all_solutions)}\n")
    
    # ✅ Added numbering of each solution
    for idx, sol in enumerate(all_solutions, 1):
        print(f"Solution #{idx}:")
        print_solution(sol)

# ✅ Added this line to prevent console window from closing when double-clicked
input("Press Enter to exit...")


