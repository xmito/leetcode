
# Unique Paths (Medium)
# There is a robot on an m x n grid. The robot is initially located at the top-left
# corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
# (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any
# point in time. Given the two integers m and n, return the number of possible unique
# paths that the robot can take to reach the bottom-right corner. Solution:
# Constraints:
# 1 <= m, n <= 100

# Time complexity: O(m * n) - we have to compute number unique paths for each position
# Space complexity: O(m * n) - store unique paths for each position
def uniquePaths(m: int, n: int) -> int:
    t = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            t[i][j] = t[i - 1][j] + t[i][j - 1]

    return t[m - 1][n - 1]


# Another possible solution is to derive number of unique paths mathematically. The
# problem is a classical combinatorial problem:
# There are h+v moves to do from start to finish, h = m − 1 horizontal moves, and
# v = n − 1 vertical ones. One could choose when to move to the right, i.e. to define
# h horizontal moves, and that will fix vertical ones. Or, one could choose when to
# move down, i.e. to define v vertical moves, and that will fix horizontal ones. In
# other words, we're asked to compute in how many ways one could choose p elements
# from p + k elements. This can be C(h+v, v) or C(h+v, h)
# Time complexity: Depends on factorial algorithm. Standard algorithm requires
# O(kˆ2logk) time and gives worse solution than one above. Peter Borwein solution
# (factorial as a product of prime numbers) in O(k(logkloglogk)ˆ2) gives better bound
# Space complexity: O(1)
# https://www.sciencedirect.com/science/article/abs/pii/0196677485900069
# http://www.luschny.de/math/factorial/description.html
from math import factorial
def uniquePathsFactorial(m: int, n: int) -> int:
    return int(factorial(m + n - 2)/(factorial(m - 1) * factorial(n - 1)))


if __name__ == "__main__":
    res = uniquePaths(3, 7)
    assert res == 28

    res = uniquePaths(3, 2)
    assert res == 3
