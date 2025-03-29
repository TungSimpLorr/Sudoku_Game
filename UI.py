import numpy as np
import random

def is_valid(board, row, col, num):
    # Kiểm tra hàng
    if num in board[row, :]:
        return False
    
    # Kiểm tra cột
    if num in board[:, col]:
        return False
    
    # Kiểm tra ô 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    box = board[start_row:start_row+3, start_col:start_col+3]
    if num in box:
        return False
    
    return True

def backtrack(board):
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row, col] = num
                        if backtrack(board):
                            return True
                        board[row, col] = 0
                return False
    return True

def sinh_bang():
    
    # tao bang trong 
    board = np.zeros((9, 9), dtype=int)
    
    # sinh so ngau nhien
    for _ in range(10):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row, col] == 0 and is_valid(board, row, col, num):
            board[row, col] = num
    
    # goi thuat toan quay lui
    backtrack(board)
    return board

def tao_bang_choi(solution):
    # tao bang choi co o bi an  
    board = solution.copy()
    so_o_bi_an = random.randint(40, 50)
    while so_o_bi_an > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row, col] != 0:
            board[row, col] = 0
            so_o_bi_an -= 1
    return board 