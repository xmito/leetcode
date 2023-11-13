from typing import List

# Sort Colors (Medium)
# Given an array nums with n objects colored red, white, or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order red,
# white, and blue. We will use the integers 0, 1, and 2 to represent the color red,
# white, and blue, respectively. You must solve this problem without using the
# library's sort function.
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

def sortColorsInitial(nums: List[int]) -> None:
    i = 0
    repl = len(nums) - 1
    to_repl = 0

    while i < len(nums) and to_repl < 2:
        while i < repl:
            if nums[i] == to_repl:
                i = i + 1
                continue

            # Identify first value to replace
            while repl > i and nums[repl] != to_repl:
                repl -= 1
            if repl <= i:
                break

            nums[i], nums[repl] = nums[repl], nums[i]
            i = i + 1

        to_repl = to_repl + 1
        repl = len(nums) - 1


# Time complexity: O(n)
# Space complexity: O(1)
def sortColors(nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0 (rightmost boundary of zeros)
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2 (leftmost boundary for twos)
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


if __name__ == "__main__":
    colors = []
    sortColors(colors)
    print(colors)
    assert colors == []

    colors = [2]
    sortColors(colors)
    print(colors)
    assert colors == [2]

    colors = [2,1]
    sortColors(colors)
    print(colors)
    assert colors == [1,2]

    colors = [2,2,1]
    sortColors(colors)
    print(colors)
    assert colors == [1,2,2]

    colors = [2,0,1]
    sortColors(colors)
    print(colors)
    assert colors == [0,1,2]

    colors = [2,0,2,1,1]
    sortColors(colors)
    print(colors)
    assert colors == [0,1,1,2,2]

    colors = [2,0,1]
    sortColors(colors)
    print(colors)
    assert colors == [0,1,2]
