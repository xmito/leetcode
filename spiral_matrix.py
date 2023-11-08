from typing import List
from itertools import cycle

# Spiral Matrix (Medium)
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Constraints
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

# Time complexity: O(n * m) because we iterate over each position once
# Space complexity: O(1), we dont count in result list
# Solution based on marking visited positions with None
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    n = len(matrix)
    m = len(matrix[0])
    result = []
    if m == 0:
        return result

    pos = [0, 0]
    offsets = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    off = next(offsets)

    while True:
        result.append(matrix[pos[0]][pos[1]])
        matrix[pos[0]][pos[1]] = None

        while pos[0] + off[0] < n and pos[1] + off[1] < m and matrix[pos[0] + off[0]][pos[1] + off[1]] is not None:
            pos[0] = pos[0] + off[0]
            pos[1] = pos[1] + off[1]
            result.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = None
       
        off = next(offsets)
        if pos[0] + off[0] >= n or pos[1] + off[1] >= m or matrix[pos[0] + off[0]][pos[1] + off[1]] is None:
            break
        pos[0] = pos[0] + off[0]
        pos[1] = pos[1] + off[1]

    return result


# Other solution based on setting boundaries
# Time complexity: O(n * m)
# Space complexity: O(1), we don't count in result list
def spiralOrderBoundaries(matrix: List[List[int]]) -> List[int]:
    result = []
    rows, columns = len(matrix), len(matrix[0])
    up = left = 0
    right = columns - 1
    down = rows - 1

    while len(result) < rows * columns:
        # Traverse from left to right.
        for col in range(left, right + 1):
            result.append(matrix[up][col])

        # Traverse downwards.
        for row in range(up + 1, down + 1):
            result.append(matrix[row][right])

        # Make sure we are now on a different row.
        if up != down:
            # Traverse from right to left.
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[down][col])

        # Make sure we are now on a different column.
        if left != right:
            # Traverse upwards.
            for row in range(down - 1, up, -1):
                result.append(matrix[row][left])

        left += 1
        right -= 1
        up += 1
        down -= 1

    return result


if __name__ == "__main__":
    res = spiralOrder([[]])
    print(res)
    assert res == []

    res = spiralOrder([[1]])
    print(res)
    assert res == [1]

    res = spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    print(res)
    assert res == [1,2,3,6,9,8,7,4,5]

    res = spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(res)
    assert res == [1,2,3,4,8,12,11,10,9,5,6,7]
