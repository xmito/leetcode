from typing import List

# Jump Game (Medium)
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105


# Backtracking brute force solution
# Time complexity: O(2ˆn) - we are exploring all possible ways of jumping from the first
# to the last position. There are 2ˆn possible jump sequences (each position is or is not
# in a jump sequence). We can express number of possible jumps recursively. Let T(x) be the
# number of possible ways to jump from x to n. T(n) = 1 trivially and from position x, we
# can jump to all positions i following x and from there in T(i) ways to the final
# position n. T(x) = Sum for i in (x+1, n) T(i) = 2 * T(x + 1). By induction assume that
# T(x) = 2ˆ(n - x - 1) and we can prove T(x - 1) = 2ˆ(n - (x - 1) - 1). Since we start from
# position 1, T(1) = 2ˆ(n-2).
# Space complexity: O(n) - recursion depth
def canJumpBrute(nums: List[int]):
    n = len(nums)

    def canJumpRecursive(i: int, j: int) -> bool:
        if i == j:
            return True

        last = min(i + nums[i], n - 1)
        for k in range(last, i, -1):
            if canJumpRecursive(k, j):
                return True
        
        return False

    return canJumpRecursive(0, n - 1)


# Dynamic programming solution
# Time complexity: O(nˆ2) - There are n positions for which we compute reachability of
# the last position. The longest jump from each position is bounded by n
# Space complexity: O(n) - store reachability for positions
def canJumpDynamic(nums: List[int]) -> bool:
    n = len(nums)
    reachable = [False] * n
    reachable[n - 1] = True

    for i in range(n - 2, -1, -1):
        maxjump = min(i + nums[i], n - 1)
        for j in range(i + 1, maxjump + 1):
            if reachable[j]:
                reachable[i] = True
                break
    return reachable[0]


# Greedy solution
# From a given position, when we try to see if we can jump to a GOOD position, we only
# ever use one - the first one (see the break statement). In other words, the left-most
# one. If we keep track of this left-most GOOD position as a separate variable, we can
# avoid searching for it in the array. Not only that, but we can stop using the array
# altogether.
# Time complexity: O(n)
# Space complexity: O(1)
def canJump(nums: List[int]) -> int:
    n = len(nums)
    left = n - 1
    for i in range(n - 2, -1, -1):
        if left <= i + nums[i]:
            left = i

    return left == 0


# Greedy solution improved
# The only thing this algorithm does differently is that it computes left to right instead
# of right to left. Instead of the leftmost reachable position, we keep the rightmost
# reachable position and update it whenever we encounter position from which we can reach
# more distant position than the current rightmost position. It has multiple advantages:
# * If we encounter position i (in left to right loop) that is larger than the rightmost
#   reachable position, we know that any position larger or equal i is also not reachable
#   and we can return immediately.
# * If there is a position with large jump number at the start of the list, that covers
#   the last position, we can detect that early and suspend further search
def canJump(nums: List[int]) -> int:
    n = len(nums)
    last = nums[0]
    for i in range(1, n):
        if i > last or last >= n - 1:
            break

        if i + nums[i] > last:
            last = i + nums[i]

    return last >= n - 1


if __name__ == "__main__":
    res = canJump([2,3,1,1,4])
    print(res)
    assert res == True

    res = canJump([3,2,1,0,4])
    print(res)
    assert res == False
