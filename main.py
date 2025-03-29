import tkinter as tk
from sudoku_game import SudokuGame

def main():
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop() # chay game 

if __name__ == "__main__":
    main() 