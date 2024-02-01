

# Palindrome number (Easy)
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Constraints:
# -2ˆ31 <= x <= 2ˆ31 - 1

# Let n be number of digits in number
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def isPalindromeDummy(x: int) -> bool:
        xstr = str(x)
        rxstr = xstr[::-1]
        if rxstr[-1] == '-':
            rxstr = rxstr[:-1]
        return xstr == rxstr


MAX = 2**31 - 1
MIN = -2**31
def reverse(x: int) -> int:
    res = 0
    sign = 1
    if x < 0:
        sign = -1
        x = abs(x)

    init_zero = True
    while x:
        value = x % 10
        if value > 0 or not init_zero:
            if res > (MAX - value) // 10:
                return 0
            res = res * 10 + value
        x = (x - value) // 10
        init_zero = False

    if sign == -1 and res > abs(MIN):
        return 0

    return sign * res


# Uses reverse function from "Reverse Integer" issue
# Let n be input number
# TIME COMPLEXITY: O(logn) - division by 10 in reverse procedure
# SPACE COMPLEXITY: O(1)
def isPalindrome(x: int) -> bool:
    rx = reverse(x)
    if rx < 0:
        rx *= -1
    return x == rx


# TIME COMPLEXITY: O(logn) - division by 10 in a loop
# SPACE COMPLEXITY: O(1)
def isPalindromeHalf(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x > 0):
        return False

    res = 0
    while res < x:
        res = res * 10 + x % 10
        x /= 10

    return res == x or x == res / 10


if __name__ == "__main__":
    ret = isPalindromeHalf(121)
    assert ret == True

    ret = isPalindromeHalf(-121)
    assert ret == False

    ret = isPalindromeHalf(10)
    assert ret == False
