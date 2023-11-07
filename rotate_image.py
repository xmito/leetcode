from typing import List

# Rotate image (Medium)
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation
# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# We can decompose issue of rotating matrix to subproblems, where each
# subproblems consists of rotating numbers at the circumference of sub
# matrices. For example, for 4x4 matrix, we first rotate numbers at cir
# cumference and then also numbers at circumference off the 2x2 submatrix
def rotateCyclic(matrix: List[List[int]]) -> None:
    n = len(matrix)

    def r(coord, dim, off):
        coord = (coord[0] - off, coord[1] - off)
        return (coord[1] + off, (dim - 1) - coord[0] + off)
        # return (coord[1], (dim - 1) - coord[0] + off)

    def rotaten(matrix: List[List[int]], offset=0) -> None:
        # Compute dimension for current problem
        dim = n - 2 * offset
        if dim <= 1:
            return

        for i in range(dim - 1):
            fx, fy = (offset, i + offset)
            value = matrix[fx][fy]

            tx, ty = r((fx, fy), dim, offset)
            while True:
                other = matrix[tx][ty]
                matrix[tx][ty] = value

                if (tx, ty) == (fx, fy):
                    break

                tx, ty = r((tx, ty), dim, offset)
                value = other

    for offset in range((n + 1) // 2):
        rotaten(matrix, offset=offset)


# Easier solution, first transpose matrix and then reflect each row
# Time complexity: O(N) linear in number of matrix cells
# Space complexity: O(1)
def transpose(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reflect(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        j, k = 0, n - 1
        while j < k:
            matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
            j += 1
            k -= 1

def rotate(matrix: List[List[int]]) -> None:
    transpose(matrix)
    reflect(matrix)


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(matrix)
    print(matrix)
    assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]