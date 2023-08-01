from sudoku import Sudoku

if __name__ == "__main__":
    sudoku_board = [
        [0, 6, 0, 5, 0, 3, 0, 8, 0],
        [0, 0, 9, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 1, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0]
    ]
    sudoku = Sudoku(sudoku_board)
    sudoku.init_board()
    sudoku.show_result()
    