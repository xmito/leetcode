from math import e, log

# Sqrt(x) (Easy)
# Given a non-negative integer x, return the square root of x rounded down to the
# nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Constraints:
# 0 <= x <= 2ˆ31 - 1


# We can use relationship sqrt(x) = eˆ(0.5 * logx)
# Time complexity: O(1)
# Space complexity: O(1)
def mySqrtCheat(x):
    if x < 2:
        return x
    
    left = int(e**(0.5 * log(x)))
    right = left + 1
    return left if right * right > x else right


# We can use relationship sqrt(x) = 2 x sqrt(x/4) and use bit shifts
# such that mySqrtHalve(x) = mySqrtHalve(x >> 2) << 1
# Time complexity: O(logn) - master theorem
# Space complexity: O(logn) - recursion stack
def mySqrtHalve(x: int) -> int:
    if x < 2:
        return x
    
    left = mySqrtHalve(x >> 2) << 1
    right = left + 1
    return left if right * right > x else right


# For x>=2, square root is smaller than x/2 and larger than 0 (0 < sqrt(x) < x/2)
# Since we are looking for integer, we use binary search on sorted integers
# Time complexity: O(logn)
# Space complexity: O(1)
def mySqrtBinary(x: int) -> int:
    if x < 0:
        raise ValueError
    elif x < 2:
        return x

    left, right = 2, x // 2
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square > x:
            right = mid - 1
        elif square < x:
            left = mid + 1
        else:
            return mid

    return right

# Newton method: x_k+1 = 0.5 * [x_k + x/x_k] converges to sqrt(x) if x_0 = x
# Time complexity: O(logn)
# Space complexity: O(1)
def mySqrtNewton(x):
    if x < 2:
        return x
    
    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 1:
        x0 = x1
        x1 = (x0 + x / x0) / 2        
        
    return int(x1)


if __name__ == "__main__":
    res = mySqrtBinary(2)
    print(res)
    assert res == 1

    res = mySqrtBinary(4)
    print(res)
    assert res == 2

    res = mySqrtBinary(8)
    print(res)
    assert res == 2
