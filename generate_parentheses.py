from typing import List

# Generate Parentheses (Medium)
# Given n pairs of parentheses, write a function to generate all
# combinations of well-formed parentheses.
# Constraints
# 1 <= n <= 8
# Let F(n) denote valid strings of length 2n. The problem F(n) can be decomposed
# into smaller subproblems of generating valid strings of smaller lengths. By
# leveraging solutions to these subproblems we can construct solution for the original
# problem. We can decompose F(n) into F(0)+F(n), F(1)+F(n-1) ... F(n)+F(0), but problem
# F(n) repeats itself (it is computed multiple times). Instead, we can use
# '( F[0] ) + F[n-1]', '( F[1] ) + F[n - 2]' ... '( F[n - 1] ) + F[0]'
# Number of solutions is the same as nth Catalan number. Time complexity is
# O(4ˆn / sqrt(n)) and space complexity O(n)
def generateParentheses(n: int) -> List[str]:
    if n == 0:
        return [""]
    
    answer = []
    for left_count in range(n):
        for left_string in generateParentheses(left_count):
            for right_string in generateParentheses(n - 1 - left_count):
                answer.append("(" + left_string + ")" + right_string)
    
    return answer


if __name__ == "__main__":
    res = generateParentheses(3)
    print(res)
    assert res == ['()()()', '()(())', '(())()', '(()())', '((()))']

    res = generateParentheses(1)
    print(res)
    assert res == ["()"]
