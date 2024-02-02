from typing import List
from bisect import bisect, insort


# Two Sum (Easy)
# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target. You may assume that each
# input would have exactly one solution, and you may not use the same element
# twice. You can return the answer in any order.
# Constraints:
# 2 <= nums.length <= 10ˆ4
# -10ˆ9 <= nums[i] <= 10ˆ9
# -10ˆ9 <= target <= 10ˆ9
# Only one valid answer exists.


# TIME COMPLEXITY: O(nˆ2) - For ith number we need to check i remnants
# SPACE COMPLEXITY: O(n) - To store remnants
def twoSumBrute(nums: List[int], target: int) -> List[int]:
    remnants = []
    for i, num in enumerate(nums):
        remnant = target - num
        try:
            index = remnants.index(remnant)
            return index, i
        except ValueError:
            pass
        remnants.append(num)


# TIME COMPLEXITY: O(nlogn)
# SPACE COMPLEXITY: O(n)
def twoSumBisect(nums: List[int], target: int) -> List[int]:
    remnants = []
    for idx, num in enumerate(nums):
        try:
            rem = target - num
            rem_idx = bisect(remnants, rem, key=lambda x: x[0])
            if remnants[rem_idx - 1][0] == rem:
                _, value_idx = remnants[rem_idx - 1]
                return idx, value_idx
        except IndexError:
            pass
        insort(remnants, (num, idx), key=lambda x: x[0])


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    remnants = {}
    for i, num in enumerate(nums):
        remnant = target - num
        if remnant in remnants:
            return [remnants[remnant], i]
        remnants[num] = i


if __name__ == "__main__":
    ret = twoSum([2, 7, 11, 15], target=9)
    print(ret)
    assert ret == [0, 1]

    ret = twoSum([3, 2, 4], target=6)
    print(ret)
    assert ret == [1, 2]

    ret = twoSum([3, 3], target=6)
    print(ret)
    assert ret == [0, 1]
