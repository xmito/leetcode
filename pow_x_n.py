
# Pow(x, n) (Medium)
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn)
# Constraints:
# -100.0 < x < 100.0
# -2ˆ31 <= n <= 2ˆ31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10ˆ4 <= xˆn <= 10ˆ4

# First try:
def myPowIterative(x: float, n: int) -> float:
    if n == 0:
        return 1

    if x == 0:
        return x

    if n < 0:
        x = 1 / x
        n = abs(n)


    cres = x
    cpower = 1
    while cpower < n:

        res = x
        power = 1
        remaining = n - cpower
        while 2 * power < remaining:
            res *= res
            power = power * 2

        cres *= res
        cpower += power

    return cres

# Time complexity: O(logn) assuming multiplication takes constant
# Space complexity: O(logn) (stack...)
def myPow(x: float, n: int) -> float:
    if n == 0: return 1
    if x == 0: return 0
    if n < 0:
        x = 1 / x
        n = abs(n)
    
    if n % 2:
        return x * myPow(x * x, (n - 1) / 2)
    return myPow(x * x, n / 2)


if __name__ == "__main__":
    res = myPow(2.00000, n=10)
    print(res)
    assert res == 1024.00000

    res = myPow(2.10000, n=3)
    print(res)
    assert res == 9.26100

    res = myPow(2.00000, n=-2)
    print(res)
    assert res == 0.25000
