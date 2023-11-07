
# Valid Parentheses (Easy)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# Constraints
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
OPENING = ['(', '{', '[']
CLOSING = [')', '}', ']']

def isValid(s: str) -> bool:
    stack = []
    for bracket in s:
        if bracket in CLOSING:
            try:
                idx = CLOSING.index(bracket)
                value = stack.pop()
                if value != OPENING[idx]:
                    return False
            except IndexError:
                return False
        else:
            stack.append(bracket)
    return len(stack) == 0


if __name__ == "__main__":
    res = isValid("()")
    assert res == True

    res = isValid("()[]{}")
    assert res == True

    res = isValid("(]")
    assert res == False