from typing import List

# Jump Game II (Medium)
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0]. Each element nums[i] represents the
# maximum length of a forward jump from index i. In other words, if you
# are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]
# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

# Correctness:
# Lemma: At the start of ith iteration of outer loop, indices interval [lo, hi]
# contains indices reachable with minimum number of jumps i - 1
# Proof:
#   Base case: for i = 1, interval is [0, 0] and each of these indices is reachable in 0 jumps
#   Induction hypothesis: Assume the statement is true for arbitrary i
#   Induction step: At the start of i + 1 iteration, [lo, hi] indices are reachable in
#       i steps. For the i + 1 iteration, we compute indices reachable from [lo, hi].
#       Since 0 <= nums[k] <= 1000, we can either reach indices from the same interval
#       [lo, hi] (that are reachable with minimum number of steps i - 1) or not yet
#       discovered indices larger than hi, that are reachable with i jumps. This is also
#       the minimum number of jumps, because indices from they were discovered have 
#       minimum number of jumps i - 1.
# Since it is guaranteed to reach nums[i - 1], there will be iteration i that will contain
# i - 1 index in indices interval [lo, hi] and algorithm will return the minimum number of jumps
# Time complexity: O(n) - each index is examined exactly once over all
# iterations of outer loop and amount of work done for each index is O(1)
# Space complexity: O(1)
def jump(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    
    # lo is furthest starting index of the current jump
    # hi is furthest reachable index of the current jump
    lo, hi = 0, 0
    for i in range(1, len(nums) + 1):
        nlo, nhi = hi + 1, 0
        for j in range(lo, hi + 1):
            nhi = max(nhi, j + nums[j])
        if nhi >= len(nums) - 1:
            break
        # If it was not guaranteed to reach nums[n - 1]
        # elif nhi < nlo:
        #    return -1
        lo, hi = nlo, nhi
    return i


if __name__ == "__main__":
    res = jump([1,1,1,1])
    print(res)
    assert res == 3

    res = jump([2,3,1,1,4])
    print(res)
    assert res == 2

    res = jump([2,3,0,1,4])
    print(res)
    assert res == 2
