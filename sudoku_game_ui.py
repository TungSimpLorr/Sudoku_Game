import tkinter as tk
from tkinter import messagebox
import numpy as np
from sudoku_xuly import sinh_bang , tao_bang_choi

class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Game")
        self.master.geometry("450x550")
        
        # Khởi tạo bảng Sudoku
        self.board = np.zeros((9, 9), dtype=int)
        self.solution = np.zeros((9, 9), dtype=int)
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        
       # tieu de 
        self.title_label = tk.Label(master, text="Sudoku Game", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)
        
        # tao khung chua bang
        self.game_frame = tk.Frame(master, borderwidth=2, relief=tk.RAISED)
        self.game_frame.pack(padx=20, pady=10)
        
        # Tạo bảng Sudoku
        self._create_board()
        
        # Nút chức năng
        self._create_buttons()
        
        # Tạo bảng Sudoku mới
        self._generate_sudoku()
    
    def _create_board(self):
        for row in range(9):
            for col in range(9):
                # Tạo viền cho các ô để phân biệt các vùng 3x3
                cell = tk.Entry(self.game_frame, 
                                width=3, 
                                font=("Arial", 20), 
                                justify='center',
                                borderwidth=2 if row % 3 == 0 or col % 3 == 0 else 1)
                cell.grid(row=row, column=col, padx=1, pady=1)
                
                # Lưu tham chiếu đến ô
                self.cells[row][col] = cell
                
                # Giới hạn nhập từ 1-9
                vcmd = (self.master.register(self._validate_input), '%P')
                cell.config(validate='key', validatecommand=vcmd)
    
    def _validate_input(self, new_value):
        # Chỉ cho phép nhập số từ 1-9 hoặc rỗng
        return new_value == "" or (len(new_value) <= 1 and new_value in "123456789")
    
    def _create_buttons(self):
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)
        
        # Tạo các nút chức năng
        buttons = [
            ("Kiểm tra", self._check_solution),
            ("Giải", self._solve_sudoku),
            ("Chơi mới", self._generate_sudoku)
        ]
        
        for text, command in buttons:
            btn = tk.Button(button_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=5)
    
    def _generate_sudoku(self):
        # Xóa bảng cũ
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.config(state=tk.NORMAL, bg='white')
                cell.delete(0, tk.END)
        
        # Sinh bảng giải
        self.solution = sinh_bang()
        
        # Tạo bảng chơi
        self.board = tao_bang_choi(self.solution)
        
        # Cập nhật giao diện
        self._update_board()
    
    def _update_board(self):
        # Cập nhật giao diện với bảng Sudoku hiện tại
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                value = self.board[row][col]
                
                # Xóa nội dung và trạng thái
                cell.delete(0, tk.END)
                cell.config(state=tk.NORMAL, bg='white')
                
                # Điền số nếu có
                if value != 0:
                    cell.insert(0, str(value))
                    cell.config(state=tk.DISABLED, disabledbackground='lightgray')
    
    def _check_solution(self):
        # Đặt lại màu nền
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.config(bg='white')
        
        # Kiểm tra lời giải của người chơi
        is_correct = True
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                
                # Bỏ qua các ô đã điền sẵn
                if self.board[row][col] != 0:
                    continue
                
                # Lấy giá trị người chơi nhập
                try:
                    player_value = int(cell.get() or 0)
                except ValueError:
                    player_value = 0
                
                # So sánh với lời giải
                if player_value != self.solution[row, col]:
                    cell.config(bg='red')
                    is_correct = False
                else:
                    cell.config(bg='green')
        
        # Thông báo kết quả
        if is_correct:
            messagebox.showinfo("Chúc mừng!", "Bạn đã giải Sudoku thành công!")
    
    def _solve_sudoku(self):
        # Hiển thị lời giải hoàn chỉnh
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                cell.config(state=tk.NORMAL)
                cell.delete(0, tk.END)
                cell.insert(0, str(self.solution[row, col]))
                cell.config(state=tk.DISABLED, disabledbackground='lightgreen') 