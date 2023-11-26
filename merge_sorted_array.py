from typing import List

# Merge Sorted Array (Easy)
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing
# order, and two integers m and n, representing the number of elements in nums1
# and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be
# stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged, and the last
# n elements are set to 0 and should be ignored. nums2 has a length of n.
# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10ˆ9 <= nums1[i], nums2[j] <= 10ˆ9


# Time complexity: O(m + n) - merge each element of sequences
# Space complexity: O(1)
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    k = m + n - 1
    i, j = m - 1, n - 1
    while i != k and i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


if __name__ == "__main__":
    array = [4,5,6,0,0,0]
    merge(array, 3, [1,2,3], 3)
    print(array)
    assert array == [1,2,3,4,5,6]

    array = [1,2,3,0,0,0]
    merge(array, 3, [2,5,6], 3)
    print(array)
    assert array == [1,2,2,3,5,6]

    array = [1]
    merge(array, 1, [], 0)
    print(array)
    assert array == [1]

    array = [0]
    merge(array, 0, [1], 1)
    print(array)
    assert array == [1]
