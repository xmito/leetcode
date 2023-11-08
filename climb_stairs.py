

# Climb Stairs (Easy)
# You are climbing a staircase. It takes n steps to reach the top. Each time you
# can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Constraints:
# 1 <= n <= 45
def climbStairs(n: int) -> int:
    r = [0] * (n + 2)
    r[1], r[2] = 1, 2
    for i in range(3, n + 1):
        r[i] = r[i - 1] + r[i - 2]
    return r[n]


if __name__ == "__main__":
    res = climbStairs(2)
    print(res)
    assert res == 2

    res = climbStairs(3)
    print(res)
    assert res == 3
