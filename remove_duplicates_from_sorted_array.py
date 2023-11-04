from typing import List

# Remove Duplicates from Sorted Array (Easy)
# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The
# relative order of the elements should be kept the same. Then return the
# number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted,
# you need to do the following things:
# * Change the array nums such that the first k elements of nums contain the
# unique elements in the order they were present in nums initially. The
# remaining elements of nums are not important as well as the size of nums.
# * Return k
def removeDuplicates(nums: List[int]) -> int:
    place = None
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            if place is None:
                place = i
            continue
        
        if place:
            nums[place] = nums[i]
            place += 1
    
    return place if place else len(nums)


if __name__ == "__main__":
    nums = [1,1,2]
    prefix = removeDuplicates(nums)
    assert prefix == 2
    assert nums[:prefix] == [1,2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    prefix = removeDuplicates(nums)
    assert prefix == 5
    assert nums[:prefix] == [0,1,2,3,4]