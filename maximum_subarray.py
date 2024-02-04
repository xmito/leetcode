from typing import List


# Maximum Subarray (Medium)
# Given an integer array nums, find the  subarray with the largest sum

# Constraints:
# 1 <= nums.length <= 10ˆ5
# -10ˆ4 <= nums[i] <= 10ˆ4


# TIME COMPLEXITY: O(nˆ2)
# SPACE COMPLEXITY: O(1)
def maxSubArrayBrute(nums: List[int]) -> int:
    global_max = -float('inf')

    for i in range(len(nums)):
        local_max = 0
        for j in range(i, len(nums)):
            local_max += nums[j]
            global_max = max(global_max, local_max)
    
    return global_max

    
# TIME COMPLEXITY: O(nlogn)
# SPACE COMPLEXITY: O(logn)
def maxSubArrayDQ(nums: List[int]) -> int:
    def recurse(left, right):
        if left > right:
            return -float('inf')

        mid = (left + right) // 2
        max_left = 0
        current = 0
        for i in range(mid - 1, -1, -1):
            current += nums[i]
            max_left = max(max_left, current)

        max_right = 0
        current = 0
        for i in range(mid + 1, len(nums)):
            current += nums[i]
            max_right = max(max_right, current)

        mid_sub = max_left + max_right + nums[mid]
        left_sub = recurse(left, mid - 1)
        right_sub = recurse(mid + 1, right)

        return max(left_sub, mid_sub, right_sub)

    return recurse(0, len(nums) - 1)


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def maxSubArray(nums: List[int]) -> int:
    global_max = -float('inf')
    local_max = 0
    for i in range(len(nums)):
        local_max = max(nums[i], local_max + nums[i])
        global_max = max(local_max, global_max)

    return global_max


if __name__ == "__main__":
    for fun in [maxSubArray, maxSubArrayBrute, maxSubArrayDQ]:
        ret = fun([-2,1,-3,4,-1,2,1,-5,4])
        print(ret)
        assert ret == 6

        ret = fun([1])
        print(ret)
        assert ret == 1

        ret = fun([5,4,-1,7,8])
        print(ret)
        assert ret == 23
