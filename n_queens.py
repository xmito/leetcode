from typing import List, Tuple, Set

# N-Queens (Hard)
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such
# that no two queens attack each other. Given an integer n, return all distinct solutions
# to the n-queens puzzle. You may return the answer in any order. Each solution contains
# a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
# indicate a queen and an empty space, respectively.
# Constraints:
# 1 <= n <= 9

def can_place(x, y, queens):
    for xq, yq in queens:
        if yq == y or abs(xq - x) == abs(yq - y):
            return False
    return True

def create_board(queens):
    board = [['.'] * len(queens) for _ in queens]
    for x, y in queens:
        board[x][y] = 'Q'
    return [''.join(row) for row in board]

# Time complexity: O(n! * n). First queen can be placed to n positions, second queen
# to at most n - 2 positions, third to n - 4 positions and so on. We can bound all
# possible arrangements of queens by O(n!). We have at most n queens and to determine
# if we can place each one, we do checks with complexity O(n). Thus the complexity is
# O(n! * n)
# Space complexity: O(n) to store positions of queens
def solveNQueensInitial(n: int) -> List[List[str]]:
    boards = []
    def place(queens: List[Tuple[int, int]]) -> None:
        if n - len(queens) == 0:
            boards.append(
                create_board(queens)
            )
            return

        x = len(queens)
        for y in range(n):
            if can_place(x, y, queens):
                place(queens + [(x, y)])
    
    place([])
    return boards


# Final solution (the fastest)
# Time complexity: O(n!)
# Space complexity: O(n)
def solveNQueens(n: int) -> List[List[int]]:
    boards = []
    board = [["."] * n for _ in range(n)]

    def place(
        queens: int,
        board: List[List[str]],
        diagonals: Set[int],
        antidiagonals: Set[int],
        columns: Set[int]
    ) -> None:
        if queens == 0:
            boards.append([''.join(row) for row in board])
            return
        
        x = n - queens
        for y in range(n):
            if (x - y) in diagonals or (x + y) in antidiagonals or y in columns:
                continue
            diagonals.add(x - y)
            antidiagonals.add(x + y)
            columns.add(y)
            board[x][y] = "Q"

            place(queens - 1, board, diagonals, antidiagonals, columns)
            board[x][y] = "."
            columns.remove(y)
            antidiagonals.remove(x + y)
            diagonals.remove(x - y)


    # All positions on diagonal have the same (row - col) value
    diagonals = set()
    # All positions on antidiagonal have the same (row + col) value
    antidiagonals = set()
    columns = set()
    place(n, board, diagonals, antidiagonals, columns)
    return boards
    

if __name__ == "__main__":
    res = solveNQueens(4)
    print(res)
    assert res == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

    res = solveNQueens(1)
    print(res)
    assert res == [["Q"]]