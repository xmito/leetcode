from typing import List

# Permutations (Medium)
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
# Time complexity: O(n * n!) - n! permutations and n for new string creation
# Space complexity: O(1)
def permute(nums: List[int]) -> List[List[int]]:
    permutations = [[nums[0]]]
    for i in range(1, len(nums)):
        temp = []
        for p in permutations:
            for k in range(len(p) + 1):
                temp += [p[:k] + [nums[i]] + p[k:]]
        permutations = temp
    return permutations

# More accurate complexity: O(n * (e * Γ(n+1,1)))
# K-permutations P_kˆn = n! / (n - k)! (use just k elements from n to create permutations)
# Number of nodes in a backtracking tree for the problem: sum(1, n) over n!/(n-k)!
# The sum can be expressed using e*Γ(n+1,1)−1 where Γ is incomplete gamma function
# Work at each node is given by node's depth, but we can bound it by O(n), so the
# overall complexity is O(n * (e * Γ(n+1,1)))


if __name__ == "__main__":
    res = permute([1,2,3])
    print(res)
    assert res == [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

    res = permute([0,1])
    print(res)
    assert res == [[1, 0], [0, 1]]

    res = permute([1])
    print(res)
    assert res == [[1]]