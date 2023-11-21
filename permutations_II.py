from typing import List
from collections import Counter

# Permutations II (Medium)
# Given a collection of numbers, nums, that might contain duplicates, return all
# possible unique permutations in any order.
# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

# Time complexity: O(n * n!) - it takes n steps to create a single permutation and there are n! of them
# Space complexity: O(nˆ2) - n recursive calls, each has a set of size at most n
def permuteUniqueSpace(nums: List[int]) -> List[List[int]]:
    def backtrack(start):
        if start == len(nums) - 1:
            unique_permutations.append(nums[:])
            return

        used = set()
        for i in range(start, len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])

            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    unique_permutations = []
    backtrack(0)
    return unique_permutations


# Time complexity: O(n * n!) - it takes n steps to create a single permutation and there are n! of them
# Space complexity: O(n) - O(n) Counter hash table, O(n) call stack, O(n) to keep permutation candidate
def permuteUnique(nums: List[int]) -> List[List[int]]:
    results = []
    def backtrack(comb, counter):
        if len(comb) == len(nums):
            # make a deep copy of the resulting permutation,
            # since the permutation would be backtracked later.
            results.append(list(comb))
            return

        for num in counter:
            if counter[num] > 0:
                # add this number into the current combination
                comb.append(num)
                counter[num] -= 1
                # continue the exploration
                backtrack(comb, counter)
                # revert the choice for the next exploration
                comb.pop()
                counter[num] += 1

    backtrack([], Counter(nums))

    return results

# Time complexity Sum(k=1, N) over P(N, k) - number of steps to complete exploration
# is exactly number of nodes in a tree. 


if __name__ == "__main__":
    res = permuteUnique([1,1,2])
    print(res)
    assert res == [[1,1,2],[1,2,1],[2,1,1]]

    res = permuteUnique([1,2,3])
    print(res)
    assert res == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]