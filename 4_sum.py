from typing import List

# 4Sum (Medium)
# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
# Constraints:
# 1 <= nums.length <= 200
# -10ˆ9 <= nums[i] <= 10ˆ9
# -10ˆ9 <= target <= 10ˆ9


# Time complexity O(nˆ3). For each two pairs of numbers (nˆ2), we look for another
# pair of number indices with linear O(n) complexity 
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    results = []
    n = len(nums)
    nums.sort()
    for i1 in range(n - 3):
        # Skip duplicates
        if i1 > 0 and nums[i1] == nums[i1 - 1]:
            continue
        for i2 in range(i1 + 1, n - 2):
            # Skip duplicates only if we are not at initial iteration. Why?
            # because if we move two pointers at once, we could skip a combination
            if i2 > 1 and nums[i2] == nums[i2 - 1] and i2 != i1 + 1:
                continue

            i3, i4 = i2 + 1, n - 1
            subtotal = nums[i1] + nums[i2]
            while i3 < i4:
                if subtotal + nums[i3] + nums[i4] > target:
                    i4 -= 1
                elif subtotal + nums[i3] + nums[i4] < target:
                    i3 += 1
                else:
                    result = [nums[i1], nums[i2], nums[i3], nums[i4]]
                    results.append(result)
                    # Move two pointers at once, because if we moved only one
                    # numbers at i3 and i4 would not sum up with i2, i3 to target
                    while i3 < i4 and nums[i3] == result[2]:
                        i3 += 1
                    while i3 < i4 and nums[i4] == result[3]:
                        i4 -= 1
    return results


if __name__ == "__main__":
    res = fourSum([1,0,-1,0,-2,2], target=0)
    print(res)
    assert res == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    res = fourSum([2,2,2,2,2], target=8)
    print(res)
    assert res == [[2,2,2,2]]