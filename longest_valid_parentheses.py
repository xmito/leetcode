

# Longest Valid Parentheses (Hard)
# Given a string containing just the characters '(' and ')', return the
# length of the longest valid (well-formed) parentheses substring

# Constraints:
# 0 <= s.length <= 3 * 10ˆ4
# s[i] is '(', or ')'.


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def longestValidParenthesesStack(s: str) -> int:
    stack = [-1]
    sublen = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
                sublen = max(sublen, i - stack[-1])
            except IndexError:
                stack.append(i)

    return sublen


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def longestValidParenthesesConstantSpace(s: str) -> int:
    left, right = 0, 0
    result = 0

    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        elif s[i] == ')':
            right += 1

        if left < right:
            left, right = 0, 0
            continue
        
        if left == right:
            result = max(result, left + right)

    left, right = 0, 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ')':
            right += 1
        elif s[i] == '(':
            left += 1

        if left > right:
            left, right = 0, 0
            continue

        if left == right:
            result = max(result, left + right)

    return result


# Dynamic Programming solution
# Let ith position in dp list store the longest valid parentheses substring ending
# at position i. Recursive relationship for dp[i]
# 0                                     if s[i] == '('
# dp[i - 2] + 2                         if s[i] == ')' and s[i - 1] == '('
# dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]] if s[i] == ')' and s[i - 1] == ')' and s[i - 1 - dp[i - 1]] == '('
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
def longestValidParenthesesDynamic(s: str) -> int:
    n = len(s)
    dp = [0] * n
        
    for end in range(1, n):
        if s[end] == '(':
            continue
        elif s[end - 1] == '(' and s[end] == ')':
            dp[end] = 2
            if end - 2 >= 0:
                dp[end] += dp[end - 2]
        elif s[end - 1] == ')' and s[end] == ')' and \
            end - 1 - dp[end - 1] >= 0 and s[end - 1 - dp[end - 1]] == '(':
            dp[end] = dp[end - 1] + 2 + dp[end - 2 - dp[end - 1]]

    return max(dp) if dp else 0


if __name__ == "__main__":
    for fun in [
        longestValidParenthesesConstantSpace,
        longestValidParenthesesDynamic,
        longestValidParenthesesStack,
    ]:
        ret = fun("(()))())(")
        print(ret)
        assert ret == 4

        ret = fun("(()")
        print(ret)
        assert ret == 2

        ret = fun(")()())")
        print(ret)
        assert ret == 4

        ret = fun("")
        print(ret)
        assert ret == 0
