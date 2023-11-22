from typing import List

# Word Search (Medium)
# Given an m x n grid of characters board and a string word, return true if word exists
# in the grid. The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same letter cell
# may not be used more than once.
# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Time complexity: O(n * 3ˆl) - where n is number of cells and l is length of word. dfs
# function is called at most once for each board cell and from each cell during traversal,
# we can pick at most 3 directions to continue recursion (with exception of initial position)
# Space complexity: O(l) - l is length of word and also depth of stack for recursive dfs calls
def exist(board: List[List[str]], word: str) -> bool:
    n = len(board)
    m = len(board[0])

    def dfs(i, j, start) -> bool:
        if board[i][j] == "#" or board[i][j] != word[start]:
            return False

        if start == len(word) - 1:
            return True

        store, board[i][j] = board[i][j], "#"
        result = False

        if i > 0:
            result |= dfs(i - 1, j, start + 1)
        if i < n - 1:
            result |= dfs(i + 1, j, start + 1)
        if j > 0:
            result |= dfs(i, j - 1, start + 1)
        if j < m - 1:
            result |= dfs(i, j + 1, start + 1)

        board[i][j] = store
        return result

    for i in range(n):
        for j in range(m):
            if board[i][j] != word[0]:
                continue
            if dfs(i, j, 0):
                return True
    
    return False


if __name__ == "__main__":
    res = exist([["a"]], "a")
    print(res)
    assert res == True

    res = exist([["a", "b"]], "ab")
    print(res)
    assert res == True

    res = exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"],
    ], "ABCCED")
    print(res)
    assert res == True

    res = exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"],
    ], "SEE")
    print(res)
    assert res == True

    res = exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], "ABCB")
    print(res)
    assert res == False