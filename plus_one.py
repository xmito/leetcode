from typing import List

# Plus One (Easy)
# You are given a large integer represented as an integer array digits, where each
# digits[i] is the ith digit of the integer. The digits are ordered from most
# significant to least significant in left-to-right order. The large integer does
# not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# Time complexity: O(n)
# Space complexity: O(1)
def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)

    carry = 1
    for i in range(n - 1, -1, -1):
        summation = digits[i] + carry
        digits[i], carry = summation % 10, summation // 10
        if carry == 0:
            break

    if carry:
        return [1] + digits

    return digits


if __name__ == "__main__":
    res = plusOne([1,2,3])
    print(res)
    assert res == [1,2,4]

    res = plusOne([4,3,2,1])
    print(res)
    assert res == [4,3,2,2]

    res = plusOne([1,9])
    print(res)
    assert res == [2,0]