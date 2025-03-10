# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    row_set = [set() for _ in range(9)]
    col_set = [set() for _ in range(9)]
    grid_set = [[set() for _ in range(3)] for _ in range(3)]
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                # check row
                if board[i][j] in row_set[i]:
                    return False
                else:
                    row_set[i].add(board[i][j])
                    
                # check column
                if board[i][j] in col_set[j]:
                    return False
                else:
                    col_set[j].add(board[i][j])
                    
                # grid check
                row, col = int(i/3), int(j/3)
                if board[i][j] in grid_set[row][col]:
                    return False
                else:
                    grid_set[row][col].add(board[i][j])
    
    return True


board =[["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
