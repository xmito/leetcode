from typing import List

# Largest Rectangle in Histogram (Hard)
# Given an array of integers heights representing the histogram's bar height where the width of
# each bar is 1, return the area of the largest rectangle in the histogram.
# Constraints:
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

# The same approach as in maximal_rectangle issue
# Time complexity: O(nˆ2) - Iterate over height values and compute height, left right boundaries and maxarea
# Space complexity: O(n) - keep height, left and right boundaries
def largestRectangleAreaInitial(heights: List[int]) -> int:
    n = len(heights)
    left = [0] * n
    right = [n] * n
    max_area = 0
    for height in sorted(set(heights + [1]) - {0,}, reverse=True):
        curr_left = 0
        for i in range(n):
            if heights[i] < height:
                curr_left = i + 1
                continue
            left[i] = max(left[i], curr_left)

        curr_right = n
        for i in range(n - 1, -1, -1):
            if heights[i] < height:
                curr_right = i
                continue
            right[i] = min(right[i], curr_right)

        for i in range(n):
            max_area = max(max_area, max(heights[i] - height + 1, 0) * (right[i] - left[i]))

    return max_area


# Time Complexity: O(nˆ3) - for nˆ2 index pairs, compute the smallest height inbetween
# Space Complexity: O(1)
def largestRectangleAreaBrute(heights: List[int]) -> int:
    max_area = 0
    for i in range(len(heights)):
        for j in range(i, len(heights)):
            min_height = float('inf')
            for k in range(i, j + 1):
                min_height = min(min_height, heights[k])
            max_area = max(max_area, min_height * (j - i + 1))
    return max_area


# Time complexity: O(nˆ2) - for nˆ2 index pairs computes minimum height using previous iteration minimum height in O(1)
# Space complexity: O(1)
def largestRectangleAreaBetterBrute(heights: List[int]) -> int:
    max_area = 0
    for i in range(len(heights)):
        min_height = float('inf')
        for j in range(i, len(heights)):
            min_height = min(min_height, heights[j])
            max_area = max(max_area, min_height * (j - i + 1))
    return max_area


# Time complexity: O(nˆ2) worst-case and O(nlogn) on average (if input is not sorted)
# Space complexity: O()
def largestRectangleAreaDivide(heights: List[int]) -> int:
    def calculateArea(heights: List[int], start: int, end: int) -> int:
        if start > end:
            return 0
        min_index = start
        for i in range(start, end + 1):
            if heights[min_index] > heights[i]:
                min_index = i
        return max(
            heights[min_index] * (end - start + 1),
            calculateArea(heights, start, min_index - 1),
            calculateArea(heights, min_index + 1, end),
        )

    return calculateArea(heights, 0, len(heights) - 1)


# Approach to solution: Imagine hill of heights and consider descent that counts all possible rectangles
# Time complexity: O(n) - each height index is appended and popped once from the stack
# Space complexity: O(n) - stack for height indices
def largestRectangleArea(heights: List[int]) -> int:
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        # Every time we pop, we find out the area of rectangle formed using the current element
        # as the height of the rectangle and the difference between the the current element's
        # index pointed to in the original array and the element stack[top−1]−1 as the width
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            hindex = stack.pop()
            max_area = max(max_area, (i - stack[-1] - 1) * heights[hindex])
        stack.append(i)

    while stack[-1] != -1:
        hindex = stack.pop()
        max_area = max(max_area, (len(heights) - stack[-1] - 1) * heights[hindex])

    return max_area


if __name__ == "__main__":
    res = largestRectangleArea([2,1,2])
    print(res)
    assert res == 3

    res = largestRectangleArea([2,0,2])
    print(res)
    assert res == 2

    res = largestRectangleArea([2,1,5,6,2,3])
    print(res)
    assert res == 10

    res = largestRectangleArea([2,4])
    print(res)
    assert res == 4
