from typing import List

# Maximal Rectangle (Hard)
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# Constraints:
# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.


# Time complexity: O(nˆ3 * mˆ3) - for each two pairs of coordinates verify if it is rectangle
# of ones. We have nˆ2 * mˆ2 different rectangles and one verification costs O(n * m)
# Space complexity: O(1)
def maximalRectangleBrute(matrix: List[List[str]]) -> int:
    n = len(matrix)
    m = len(matrix[0])

    def verify(x1, y1, x2, y2):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if matrix[i][j] == "0":
                    return False
        
        return True

    
    maxcontent = 0
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    if verify(x1, y1, x2, y2):
                        content = (x2 - x1 + 1) * (y2 - y1 + 1)
                        maxcontent = max(content, maxcontent)

    return maxcontent


# For each position in matrix (from left top to bottom down), compute the longest (in-row)
# rectangle that ends in the position. In each iteration, we check also the maximum area
# rectangle by iterating over already computed values in the same column and determining
# minimum histogram height and multiplying by size of consecutive non-zero values
# Time complexity: O(nˆ2 * m) - for each position in matrix, compute maximum area rectangle above it
# Space complexity: O(n * m) - histogram matrix
def maximalRectangleHistogram(matrix: List[List[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])

    max_area = 0
    histograms = []
    for i in range(n):
        histograms.append(
            [int(value) for value in matrix[i]]
        )
        for j in range(m):
            if j > 0 and matrix[i][j] == "1":
                histograms[i][j] = histograms[i][j - 1] + 1

            min_col = float('inf')
            last = i
            for k in range(i, -1, -1):
                if histograms[k][j] == 0:
                    min_col = float('inf')
                    last = k - 1
                    continue

                min_col = min(min_col, histograms[k][j])
                max_area = max(max_area, min_col * (last - k + 1))
    
    return max_area


# Idea of this approach is to keep for each position in a row height, left and right boundaries.
# * Height is the height of consecutive ones above the position (including one in the currently considered position, otherwise 0).
# * Left boundary is the maximum index that bounds consecutive ones to the left of the considered position
# * Right boundary is the minimum index that bounds ones to the the right of currently considered position
# Algorithm iterates over cells row by row and each time updates all lists using data computed 
# in the previous row. Each position is contained in a rectangle given by height, left and right
# boundaries. These values depend on height of ones and boundaries for cells above
# Time complexity: O(n * m) - each cell is considered once and amount of work is O(1)
# Space compleity: O(n) - height, left and right boundaries
def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix: return 0

    m = len(matrix)
    n = len(matrix[0])

    left = [0] * n # initialize left as the leftmost boundary possible
    right = [n] * n # initialize right as the rightmost boundary possible
    height = [0] * n

    maxarea = 0

    for i in range(m):

        cur_left, cur_right = 0, n
        # update height
        for j in range(n):
            if matrix[i][j] == '1': height[j] += 1
            else: height[j] = 0
        # update left
        for j in range(n):
            if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1
        # update right
        for j in range(n-1, -1, -1):
            if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
            else:
                right[j] = n
                cur_right = j
        # update the area
        for j in range(n):
            maxarea = max(maxarea, height[j] * (right[j] - left[j]))

    return maxarea


if __name__ == "__main__":
    res = maximalRectangle([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"],
    ])
    print(res)
    assert res == 6

    res = maximalRectangle([["1"]])
    print(res)
    assert res == 1

    res = maximalRectangle([["0"]])
    print(res)
    assert res == 0

    res = maximalRectangle([
        ["0","1","1","0","0","1","0","1","0","1"],
        ["0","0","1","0","1","0","1","0","1","0"],
        ["1","0","0","0","0","1","0","1","1","0"],
        ["0","1","1","1","1","1","1","0","1","0"],
        ["0","0","1","1","1","1","1","1","1","0"],
        ["1","1","0","1","0","1","1","1","1","0"],
        ["0","0","0","1","1","0","0","0","1","0"],
        ["1","1","0","1","1","0","0","1","1","1"],
        ["0","1","0","1","1","0","1","0","1","1"],
    ])
    print(res)
    assert res == 10

