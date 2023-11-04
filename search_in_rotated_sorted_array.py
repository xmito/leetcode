from typing import List

# Search in Rotated Sorted Array (Medium)
# There is an integer array nums sorted in ascending order (with distinct values). Prior to
# being passed to your function, nums is possibly rotated at an unknown pivot index k
# (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index
# of target if it is in nums, or -1 if it is not in nums. You must write an algorithm with
# O(log n) runtime complexity.
# nums = [4,5,6,7,0,1,2], target = 0 => 4
# nums = [4,5,6,7,0,1,2], target = 3 => -1
# nums = [1], target = 0 => -1

# First try
def search_(nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return -1

    # Find number of rotations performed
    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            break
    else:
        i = 0
    rotations = (n - i) % n

    # Translation layer for indices
    def tr(index, n, k):
        if index >= k:
            return index - k
        return index + n - k

    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        tr_mid = tr(mid, n, rotations)
        mid_value = nums[tr_mid]

        if mid_value == target:
            return tr_mid
        elif mid_value > target:
            j = mid - 1
        else:
            i = mid + 1
    
    return -1

# Final solution
def search(nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return -1

    i, j = 0, n - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] > nums[-1]:
            i = mid + 1
        else:
            j = mid - 1

    shift = n - i

    i, j = 0, n - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[(mid - shift) % n] == target:
            return (mid - shift) % n
        elif nums[(mid - shift) % n] > target:
            j = mid - 1
        else:
            i = mid + 1

    return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    res = search(nums, target=0)
    print(res)
    assert res == 4

    nums = [4,5,6,7,0,1,2]
    res = search(nums, target=3)
    print(res)
    assert res == -1

    nums = [1]
    res = search(nums, target=0)
    print(res)
    assert res == -1