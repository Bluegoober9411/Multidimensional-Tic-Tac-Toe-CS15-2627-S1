grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]
def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)
def determine_winner(grid):
    for row in grid:
        if row[0] == row[1] == row[2]:
            return row[0]
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col]:
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    if grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]
    return "Tie"
boards = [grid_1, grid_2, grid_3, grid_4]
board_number = 1
for board in boards:
    print("Board", board_number)
    display_grid(board)
    winner = determine_winner(board)
    if winner == "Tie":
        print("Result: Tie")
    else:
        print("Result:", winner, "wins!")
    print()
    board_number += 1