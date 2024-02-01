

# Reverse Integer (Medium)
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer
# range [-2**31, 2**31 - 1], then return 0.
# Constraints:
# -2ˆ31 <= x <= 2ˆ31 - 1

# TIME COMPLEXITY: O(logn) - where n is input number
# SPACE COMPLEXITY: O(1)
MAX = 2**31 - 1
MIN = -2**31
def reverse(x: int) -> int:
    res = 0
    sign = 1
    if x < 0:
        sign = -1
        x = abs(x)

    init_zero = True  # Skip initial zeroes
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


if __name__ == "__main__":
    ret = reverse(123)
    print(ret)
    assert ret == 321

    ret = reverse(-123)
    print(ret)
    assert ret == -321

    ret = reverse(120)
    print(ret)
    assert ret == 21
