from typing import List

# First Missing Positive (Hard)
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# Observations:
# 1. Missing positive integer cannot be larger than the length of array + 1
# 2. We can ignore negative numbers and zeroes (they are not positive)
# Solution employs cyclic sort
def firstMissingPositiveCyclic(nums: List[int]) -> int:
    for i in range(len(nums)):
        if nums[i] > len(nums) or nums[i] < 1:
            continue

        pos = i
        value = nums[pos]
        while value - 1 != pos:
            other = nums[value - 1]
            nums[value - 1] = value

            pos, value = value - 1, other
            if value > len(nums) or value < 1:
                # Place negative number to initial position i from
                # which we have taken the first misplaced number
                nums[i] = -1
                break

    # Nums list is sorted and first missing positive is given by the first
    # position at which we encounter number that is out of range, else it
    # is length of nums array + 1
    for i in range(len(nums)):
        if nums[i] > len(nums) or nums[i] < 1 or nums[i] - 1 != i:
            return i + 1
    return len(nums) + 1


def firstMissingPositive(nums: List[int]) -> int:
    # Base case, verify whether the first missing positive integer
    # is missing in nums. We will use number one as replacement for
    # negative numbers, zeroes or numbers larger than nums length
    if 1 not in nums:
        return 1
    n = len(nums)

    # Replace all numbers we want to ignore with ones
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # Number a belongs to position a - 1, so we will mark number at
    # that position with minus sign to indicate that position + 1
    # value is present in array
    for i in range(n):
        a = abs(nums[i])
        nums[a - 1] = - abs(nums[a - 1])
    
    # Index of the first positive number determines first positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    # Nums list holds all values 1..n. First positive number is n + 1
    return n + 1


if __name__ == "__main__":
    res = firstMissingPositive([2,3,4,-1])
    print(f'firstMissingPositive([2,3,4,-1]) => {res}')
    assert res == 1

    res = firstMissingPositive([1,2,0])
    print(f'firstMissingPositive([1,2,0]) => {res}')
    assert res == 3

    res = firstMissingPositive([3,4,-1,1])
    print(f'firstMissingPositive([3,4,-1,1]) => {res}')
    assert res == 2

    res = firstMissingPositive([7,8,9,11,12])
    print(f'firstMissingPositive([7,8,9,11,12]) => {res}')
    assert res == 1
