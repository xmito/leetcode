from typing import List

# Find First and Last Position of Element in Sorted Array (Medium)
# Given an array of integers nums sorted in non-decreasing order, find the starting
# and ending position of a given target value. If target is not found in the array,
# return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

def searchLeft(nums: List[int], target:int) -> int:
    if not len(nums):
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if left < len(nums) and nums[left] == target:
        return left
    return -1

def searchRight(nums: List[int], target:int) -> int:
    if not len(nums):
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if right >= 0 and nums[right] == target:
        return right
    return -1

def searchRange(nums: List[int], target: int) -> List[int]:
    return [searchLeft(nums, target), searchRight(nums, target)]


if __name__ == '__main__':
    res = searchRight([1,2,3,4,5,5,8,8,8,9,9,10], target=8)
    res = searchLeft([1,2,3,4,5,5,8,8,8,9,9,10], target=8)
    print(res)
    assert res == 6

    res = searchRight([1], target=1)
    res = searchLeft([1], target=1)
    print(res)
    assert res == 0

    res = searchRight([7,8], target=7)
    res = searchLeft([7,8], target=7)
    print(res)
    assert res == 0

    res = searchRange([2,2], target=3)
    print(res)
    assert res == [-1,-1]

    res = searchRange([1], 1)
    print(res)
    assert res == [0, 0]

    res = searchRange([5,7,7,8,8,10], 8)
    print(res)
    assert res == [3,4]

    res = searchRange([5,7,7,8,8,10], 6)
    print(res)
    assert res == [-1,-1]

    res = searchRange([], target=0)
    print(res)
    assert res == [-1,-1]