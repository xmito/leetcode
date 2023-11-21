from typing import List

# Minimum Path Sum (Medium)
# Given a m x n grid filled with non-negative numbers, find a path from top left to
# bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200

# Time complexity: O(2ˆ(m + n)) - for every position we traverse (at most m + n - 2) we
# need to consider two options for next move
# Space complexity: O(m + n) - recursion depth
def minPathSumBrute(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    def minPathSumRecursive(i: int, j: int) -> int:
        if i < 0 or j < 0:
            return float('inf')
        elif i == 0 and j == 0:
            return grid[i][j]

        return grid[i][j] + min(
            minPathSumRecursive(i - 1, j),
            minPathSumRecursive(i, j - 1),
        )

    return minPathSumRecursive(m - 1, n - 1)


# Time complexity: O(m * n)
# Space complexity: O(m * n)
def minPathSumSq(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    t = [[0] * n for _ in range(m)]

    t[0][0] = grid[0][0]
    for i in range(1, m):
        t[i][0] = grid[i][0] + t[i - 1][0]
    
    for j in range(1, n):
        t[0][j] = grid[0][j] + t[0][j - 1]
    
    for i in range(1, m):
        for j in range(1, n):
            t[i][j] = min(t[i - 1][j], t[i][j - 1]) + grid[i][j]
    
    return t[m - 1][n - 1]


# Time complexity: O(m * n)
# Space complexity: O(n) - possible to do O(1) if values stored in grid
def minPathSum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    t = [grid[0][0]] * n

    for j in range(1, n):
        t[j] = grid[0][j] + t[j - 1]

    for i in range(1, m):
        temp = [0] * n
        for j in range(n):
            if j == 0:
                temp[j] = grid[i][j] + t[0]
            else:
                temp[j] = grid[i][j] + min(temp[j - 1], t[j])
        t = temp

    return t[n - 1]


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    res = minPathSum(grid)
    print(res)
    assert res == 7

    grid = [[1,2,3],[4,5,6]]
    res = minPathSum(grid)
    print(res)
    assert res == 12