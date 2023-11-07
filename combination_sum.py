from typing import List

# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers
# sum to target. You may return the combinations in any order. The same number
# may be chosen from candidates an unlimited number of times. Two combinations
# are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
# Time complexity: O(Nˆ((T/M)+1))
# N - number of candidates, T - target value, M - minimum candidate value
# Maximum depth of explored tree is bounded by T/M, so number of combinations
# we review are Nˆ(T/M) + 1. For each combination we do constant amount of work
# with exception of valid combinations (leaves) which we need to copy. If we
# assume there is constant number of them, time complexity is O(Nˆ((T/M)+1))
# Space complexity: We store one combination list over all recursive calls.
# This list has size at most T/M, hence the space complexity is O(T/M)

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    combinations = []
    def backtrack(cstart: int, combination: List[int], target: int):
        if target == 0:
            combinations.append(list(combination))
            return

        for i in range(cstart, len(candidates)):
            if candidates[i] > target:
                continue

            combination.append(candidates[i])
            backtrack(i, combination, target - candidates[i])
            combination.pop()

    backtrack(0, [], target)
    return combinations


if __name__ == '__main__':
    res = combinationSum([2,3,6,7], target=7)
    print(res)
    assert res == [[2,2,3],[7]]

    res = combinationSum([2,3,5], target=8)
    print(res)
    assert res == [[2,2,2,2],[2,3,3],[3,5]]

    res = combinationSum([2], target=1)
    print(res)
    assert res == []

    res = combinationSum([5], target=12)
    print(res)
    assert res == []

    res = combinationSum([8,7,4,3], target=11)
    print(res)
    assert res == [[8,3],[7,4],[4,4,3]]