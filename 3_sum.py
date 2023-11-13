from typing import List

# 3Sum (Medium)
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Constraints:
# 3 <= nums.length <= 3000
# -10ˆ5 <= nums[i] <= 10ˆ5

# Time complexity: O(nˆ2)
# Space complexity: O(n) due to timsort sorting
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    for i1 in range(len(nums) - 2):
        # Number at index i1 will be the smallest in a triplet of values
        if nums[i1] > 0:
            break

        # Skip duplicate solutions
        if i1 > 0 and nums[i1] == nums[i1 - 1]:
            continue
        i2, i3 = i1 + 1, len(nums) - 1
        while i2 < i3:
            total = nums[i1] + nums[i2] + nums[i3]
            if total > 0:
                i3 -= 1
            elif total < 0:
                i2 += 1
            else:
                result = [nums[i1], nums[i2], nums[i3]]
                results.append(result)
                # Skip duplicate solutions
                while i2 < i3 and nums[i2] == result[1]:
                    i2 += 1
                while i2 < i3 and nums[i3] == result[2]:
                    i3 -= 1 
    return results


# Time complexity: O(nˆ2)
# Space complexity: O(n) - timsort + seen hashset
def threeSumComplement(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSum(nums, i, res)
    return res

def twoSum(nums: List[int], i: int, res: List[List[int]]):
    seen = set()
    j = i + 1
    while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
            res.append([nums[i], nums[j], complement])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1


# Time complexity: O(nˆ2)
# Space complexity: O(n) - hashset/hashmap
def threeSumWOSorting(nums: List[int]) -> List[List[int]]:
    res, dups = set(), set()
    seen = {}
    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                # To indicate we have seen val2 in this outer loop iteration
                seen[val2] = i 
    return res


if __name__ == "__main__":
    res = threeSum([-1, 0, 1, 2, -1, 4])
    print(res)
    assert res == [[-1, -1, 2], [-1, 0, 1]]

    res = threeSum([0, 1, 1])
    print(res)
    assert res == []

    res = threeSum([0, 0, 0])
    print(res)
    assert res == [[0, 0, 0]]
