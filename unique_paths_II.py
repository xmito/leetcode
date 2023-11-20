from typing import List

# Unique Paths II (Medium)
# You are given an m x n integer array grid. There is a robot initially located at the
# top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
# (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point
# in time. An obstacle and space are marked as 1 or 0 respectively in grid. A path that
# the robot takes cannot include any square that is an obstacle. Return the number of
# possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 10ˆ9.

# Time complexity: O(n * m)
# Space complexity: O(n * m) - possible to use obstacleGrid as t list, then O(1)
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    t = [[0] * n for _ in range(m)]

    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        t[i][0] = 1
    
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break
        t[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                continue
            t[i][j] = t[i - 1][j] + t[i][j - 1]
    
    return t[m - 1][n - 1]


if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    res = uniquePathsWithObstacles(obstacleGrid)
    assert res == 2

    obstacleGrid = [[0,1],[0,0]]
    res = uniquePathsWithObstacles(obstacleGrid)
    assert res == 1
