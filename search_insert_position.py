from typing import List

# Given a sorted array of distinct integers and a target value, return the index
# if the target is found. If not, return the index where it would be if it were
# inserted in order. You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


if __name__ == '__main__':
    res = searchInsert([1,3,5,6], target=5)
    print(res)
    assert res == 2

    res = searchInsert([1,3,5,6], target=2)
    print(res)
    assert res == 1

    res = searchInsert([1,3,5,6], target=7)
    print(res)
    assert res == 4