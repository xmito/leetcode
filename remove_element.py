from typing import List

# Remove Element (Easy)
# Given an integer array nums and an integer val, remove all occurrences of
# val in nums in-place. The order of the elements may be changed. Then return
# the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:
# * Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# * Return k.
def removeElement(nums: List[int], val: int) -> int:
    place = None
    for i in range(len(nums)):
        if place is None and nums[i] == val:
            place = i
        elif place is not None and nums[i] != val:
            nums[place] = nums[i]
            place = place + 1

    return place if place is not None else len(nums)


if __name__ == "__main__":
    nums = [3,2,2,3]
    prefix = removeElement(nums, val=3)
    assert nums[:prefix] == [2,2]

    nums = [0,1,2,2,3,0,4,2]
    prefix = removeElement(nums, val=2)
    assert nums[:prefix] == [0,1,3,0,4]