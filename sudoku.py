from typing import List, Tuple


class Sudoku:
    def __init__(self, board: List[List[int]]) -> None:
        self.board = board
        self.board_file_name = "sudoku_board.txt"

    def init_board(self) -> None:
        sudoku_board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        with open(self.board_file_name, "w") as file:
            for row in sudoku_board:
                file.write(str(row) + "\n")


    def find_empty_cell(self) -> Tuple[int or None, int or None]:
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None, None

    def is_valid(self, row_line: int, col_idx: int, num: int) -> bool:
        # Check row
        for i in range(9):
            if self.board[row_line][i] == num:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col_idx] == num:
                return False

        # Check 3x3 subgrid
        start_row, start_col = 3 * (row_line // 3), 3 * (col_idx // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku(self) -> bool:
        row, col = self.find_empty_cell()
        if row is None:
            # No empty cells left; the Sudoku is solved
            return True

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve_sudoku():
                    return True

                # Backtrack
                self.board[row][col] = 0
        return False

    def show_result(self) -> None:
        self.solve_sudoku()
        for row in self.board:
            print(row)
    