from typing import List

# Subsets (Medium)
# Given an integer array nums of unique elements, return all possible subsets (the
# power set). The solution set must not contain duplicate subsets. Return the solution
# in any order.


# In each iteration add a number to existing subsets
# Time complexity: O(n * 2ˆn)
# Space complexity: O(n * 2ˆn) - we have to keep transient results
def subsetsEasy(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for num in nums:
        result += [x + [num] for x in result]
    
    return result


# Backtracking
# Power set is all possible combinations of all possible lengths, from 0 to n.
# In backtracking approach, we recurse on current subset and the lowest index
# of the first value that can be added to the subset
# Time complexity: O(n * 2ˆn) - in each backtrack call,
# Space complexity: O(n) - stack depth and curr list
def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = [[]]

    def backtrack(curr, start):
        if start == len(nums):
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            result.append(curr[:])
            backtrack(curr, i + 1)
            curr.pop()
        
    backtrack([], 0)
    return result


# Represent each subset using bitmask of length n. To generate all subsets, generate
# all possible bitmasks and enumerate all solutions from them
# Time complexity: O(n * 2ˆn)
# Space complexity: O(n * 2ˆn)
def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    output = []
    
    for i in range(2**n, 2**(n + 1)):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i)[3:]
        
        # append subset corresponding to that bitmask
        output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    
        return output


if __name__ == "__main__":
    res = subsetsEasy([1,2,3])
    print(res)
    assert res == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    res = subsetsEasy([0])
    print(res)
    assert res == [[],[0]]
