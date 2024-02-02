from typing import List


# Trapping Rain Water (Hard)
# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.
# Following solution has O(nˆ2) time complexity and O(1) spatial complexity

# Constraints:
# n == height.length
# 1 <= n <= 2 * 10ˆ4
# 0 <= height[i] <= 10ˆ5


# TIME COMPLEXITY: O(n) - Each height is iterated over twice
# SPACE COMPLEXITY: O(1)
def trapConstantSpace(heights: List[int]) -> int:
    i = 0
    units = 0
    while i < len(heights) - 1:
        h = heights[i]
        higher, hh = -1, -1
        for j in range(i + 1, len(heights)):
            if heights[j] > hh:
                higher = j
                hh = heights[j]
            if hh >= h:
                break

        for j in range(i + 1, higher):
            units += min(h, hh) - heights[j]
        i = higher
    return units


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def trapStack(heights: List[int]) -> int:
    result = 0
    stack = []

    for i in range(len(heights)):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()
            if not stack:
                break

            distance = i - stack[-1] - 1
            height = min(heights[i], heights[stack[-1]]) - heights[top]
            result += height * distance

        stack.append(i)

    return result


# Amount of water that can be trapped at certain position is equal to the minimum
# of maximum of heights to the left and right minus height at the position
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def trap(height: List[int]) -> int:
    n = len(height)
    l = [0] * n  
    r = [0] * n
    ans = 0
    lm, rm = 0, 0

    for i in range(n):
        l[i] = lm
        if lm < height[i]:
            lm = height[i]
    for i in range(n - 1, -1, -1):
        r[i] = rm
        if rm < height[i]:
            rm = height[i]
    for i in range(n):
        trapped = min(l[i], r[i]) - height[i]
        if trapped > 0:
            ans += trapped

    return ans


if __name__ == "__main__":
    ret = trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(ret)
    assert ret == 6
