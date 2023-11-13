from typing import List

# Search a 2D Matrix (Medium)
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10ˆ4 <= matrix[i][j], target <= 10ˆ4

# Time complexity: O(log n*m)
# Space complexity: O(1)
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    i, j = 0, rows * cols - 1
    while i <= j:
        mid = i + (j - i) // 2
        x, y = mid // cols, mid % cols
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] > target:
            j = mid - 1
        else:
            i = mid + 1

    return False


if __name__ == "__main__":
    matrix = [[1,1]]
    res = searchMatrix(matrix, target=2)
    assert res == False

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    res = searchMatrix(matrix, target=3)
    assert res == True

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    res = searchMatrix(matrix, target=13)
    assert res == False