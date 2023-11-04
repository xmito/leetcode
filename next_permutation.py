from typing import List

# Next Permutation (Medium)
# A permutation of an array of integers is an arrangement of its members into a sequence or
# linear order. For example, for arr = [1,2,3], the following are all the permutations of
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]. The next permutation of
# an array of integers is the next lexicographically greater permutation of its integer.
# More formally, if all the permutations of the array are sorted in one container according
# to their lexicographical order, then the next permutation of that array is the permutation
# that follows it in the sorted container. If such arrangement is not possible, the array must
# be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a
# lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.
def bisect(nums, value):
    """ 
        Returns index i such that values a[:i] are higher than value
        and values in a[i:] are lower or equal than value
    """
    i, j = 0, len(nums)
    while i < j:
        k = (i + j) // 2
        if nums[k] <= value:
            j = k
        else:
            i = k + 1
    
    return i

def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    if n == 1:
        return

    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            break
    else:
        # Digits sorted in decreasing order, reverse them
        nums.reverse()
        return

    # Else find the closest higher digit and replace them
    pos = bisect(nums[i + 1:], nums[i]) -1 + i + 1
    nums[i], nums[pos] = nums[pos], nums[i]

    # Once replaced, reverse order to ascending
    j, k = i + 1, n - 1
    while j < k:
        nums[j], nums[k] = nums[k], nums[j]
        j = j + 1
        k = k - 1

    return


if __name__ == '__main__':
    nums = [1,2,3]
    nextPermutation(nums)
    assert nums == [1,3,2]

    nums = [3,2,1]
    nextPermutation(nums)
    assert nums == [1,2,3]

    nums = [1,1,5]
    nextPermutation(nums)
    assert nums == [1,5,1]
